from pathlib import Path

hud = Path(__file__).resolve().parent
print(hud)
gui = hud.parent / "gui"
print(gui)