
import json
import time
from pathlib import Path

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


API_URL = "https://api.tcgdex.net/v2/en/cards"
OUTPUT_DIR = Path("cards")

TRAINER_TYPES = [
    "Item",
    "Supporter",
    "Tool",
    "Stadium",
    "Technical Machine",
    "Rocket's Secret Machine",
]

PAGE_SIZE = 100
IMAGE_RESOLUTION = "high"  # "high" or "low"
REQUEST_DELAY = 0.15

# Set to None to download all matching cards.
# Set to 10 to test with 10 cards per category.
MAX_CARDS_PER_TYPE = None


def create_session():
    session = requests.Session()

    retry = Retry(
        total=4,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
    )

    adapter = HTTPAdapter(max_retries=retry)

    session.mount("https://", adapter)
    session.headers.update({
        "User-Agent": "PokemonBoardGameAssetDownloader/1.0"
    })

    return session


def get_cards(session, trainer_type):
    """Fetch all cards matching one Trainer subtype."""

    cards = []
    page = 1

    while True:
        params = {
            "trainerType": f"eq:{trainer_type}",
            "pagination:page": page,
            "pagination:itemsPerPage": PAGE_SIZE,
        }

        response = session.get(
            API_URL,
            params=params,
            timeout=30
        )
        response.raise_for_status()

        batch = response.json()

        if not isinstance(batch, list):
            raise ValueError("Unexpected TCGdex response")

        if not batch:
            break

        cards.extend(batch)

        print(
            f"  Page {page}: {len(batch)} cards"
        )

        if (
            MAX_CARDS_PER_TYPE is not None
            and len(cards) >= MAX_CARDS_PER_TYPE
        ):
            cards = cards[:MAX_CARDS_PER_TYPE]
            break

        if len(batch) < PAGE_SIZE:
            break

        page += 1
        time.sleep(REQUEST_DELAY)

    return cards


def download_image(session, card, trainer_type):
    """Download one card image and return its local path."""

    card_id = card["id"]
    image_base = card.get("image")

    if not image_base:
        print(f"  No image: {card_id}")
        return None

    folder_name = trainer_type.lower().replace(" ", "_").replace("'", "")
    folder = OUTPUT_DIR / folder_name
    folder.mkdir(parents=True, exist_ok=True)

    image_path = folder / f"{card_id}.png"

    if image_path.is_file() and image_path.stat().st_size > 0:
        return image_path

    image_url = f"{image_base}/{IMAGE_RESOLUTION}.png"

    response = session.get(
        image_url,
        timeout=30
    )

    if response.status_code == 404:
        print(f"  Image unavailable: {card_id}")
        return None

    response.raise_for_status()

    image_path.write_bytes(response.content)

    time.sleep(REQUEST_DELAY)

    return image_path


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    session = create_session()

    manifest = []
    downloaded = 0
    skipped = 0

    for trainer_type in TRAINER_TYPES:
        print(f"\nFetching {trainer_type} cards...")

        cards = get_cards(session, trainer_type)

        print(f"Found {len(cards)} cards")

        for index, card in enumerate(cards, start=1):
            try:
                image_path = download_image(
                    session,
                    card,
                    trainer_type
                )

                if image_path is None:
                    skipped += 1
                    continue

                manifest.append({
                    "id": card["id"],
                    "name": card["name"],
                    "trainer_type": trainer_type,
                    "image_path": image_path.as_posix(),
                })

                downloaded += 1

                print(
                    f"[{index}/{len(cards)}] "
                    f"{card['name']}"
                )

            except requests.RequestException as error:
                skipped += 1
                print(f"Failed {card['id']}: {error}")

    manifest_path = OUTPUT_DIR / "cards.json"

    manifest_path.write_text(
        json.dumps(manifest, indent=4, ensure_ascii=False),
        encoding="utf-8"
    )

    print("\nDownload complete!")
    print(f"Cards saved: {downloaded}")
    print(f"Images unavailable/failed: {skipped}")
    print(f"Manifest: {manifest_path}")


if __name__ == "__main__":
    main()
