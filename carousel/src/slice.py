"""Slice a panorama into 8 Instagram slides (PNG + JPG), a preview strip and a zip.
usage: slice.py [out_dir] [jpg_prefix]"""
import sys, zipfile
from pathlib import Path
from PIL import Image

OUT = Path(__file__).resolve().parent.parent / (sys.argv[1] if len(sys.argv) > 1 else "out")
PREFIX = sys.argv[2] if len(sys.argv) > 2 else "apec_carousel"
pano = Image.open(OUT / "panorama.png").convert("RGB")
(OUT / "instagram").mkdir(exist_ok=True)
for i in range(8):
    s = pano.crop((i * 1080, 0, (i + 1) * 1080, 1350))
    s.save(OUT / f"slide_{i+1:02d}.png", optimize=True)
    s.save(OUT / "instagram" / f"{PREFIX}_{i+1:02d}.jpg", quality=95, subsampling=0)
prev = pano.resize((pano.width // 4, pano.height // 4), Image.LANCZOS)
gap = 6
strip = Image.new("RGB", (prev.width + gap * 7, prev.height), "white")
for i in range(8):
    strip.paste(prev.crop((i * 270, 0, (i + 1) * 270, prev.height)), (i * (270 + gap), 0))
strip.save(OUT / "preview_strip.jpg", quality=88)
with zipfile.ZipFile(OUT / f"{PREFIX}.zip", "w") as z:
    for f in sorted((OUT / "instagram").glob("*.jpg")):
        z.write(f, f.name)
