"""Slice the panorama into 8 Instagram slides (1080x1350) + preview strip."""
from pathlib import Path
from PIL import Image
OUT = Path(__file__).resolve().parent.parent / "out"
pano = Image.open(OUT / "panorama.png").convert("RGB")
for i in range(8):
    pano.crop((i * 1080, 0, (i + 1) * 1080, 1350)).save(OUT / f"slide_{i+1:02d}.png", optimize=True)
prev = pano.resize((pano.width // 4, pano.height // 4), Image.LANCZOS)
gap = 6
strip = Image.new("RGB", (prev.width + gap * 7, prev.height), "white")
for i in range(8):
    strip.paste(prev.crop((i * 270, 0, (i + 1) * 270, prev.height)), (i * (270 + gap), 0))
strip.save(OUT / "preview_strip.jpg", quality=88)
