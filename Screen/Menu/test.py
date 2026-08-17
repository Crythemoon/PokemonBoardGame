from PIL import Image

frame_paths = [
    "/mnt/data/ghostwriter_images/generated/a_pixel_art_fantasy_landscape_scene_overall_a_ser_1.png",
    "/mnt/data/ghostwriter_images/generated/a_wide_detailed_pixel_art_fantasy_landscape_scene_2_batch_1.png",
    "/mnt/data/ghostwriter_images/generated/a_wide_pixel_art_fantasy_landscape_at_sunset_sunr_3_batch_2.png",
    "/mnt/data/ghostwriter_images/generated/a_wide_colorful_pixel_art_landscape_scene_at_suns_4_batch_3.png",
]

frames = [Image.open(p).convert("RGBA") for p in frame_paths]

# Make sure every frame has the same size.
base_size = frames[0].size
frames = [img.resize(base_size, Image.Resampling.NEAREST) for img in frames]

# Convert to an optimized palette format suitable for GIF.
gif_frames = [img.convert("P", palette=Image.Palette.ADAPTIVE, colors=256) for img in frames]

output_path = "/mnt/data/pokemon_board_game_main_menu.gif"

gif_frames[0].save(
    output_path,
    save_all=True,
    append_images=gif_frames[1:],
    duration=450,   # milliseconds per frame
    loop=0,         # loop forever
    optimize=True,
    disposal=2,
)

print(output_path)
