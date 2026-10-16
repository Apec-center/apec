"""Prepare cover crops for B/C and a privacy-safe copy of the client's card photo."""
import numpy as np
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter
import card_extract as ce

A = Path(__file__).resolve().parent.parent / "assets"

# B cover: vertical 4:5 crop of the wide scene, centred on the bottle
b = Image.open(A / "b_cover.png").convert("RGB")
w = round(b.height * 4 / 5)
x0 = 2273 - round(w * 0.75)                    # bottle centre (x≈2273 in the wide scene) at 75% of the slide
b.crop((x0, 0, x0 + w, b.height)).save(A / "B1.png")

# C4: the client's photo with document number and birth date blurred
photo = Image.open(A / "real_card_photo.jpg").convert("RGB")
h = np.append(ce.coeffs(ce.DST, ce.SRC), 1).reshape(3, 3)      # flat card -> photo


def to_photo(x, y):
    u, v, s = h @ np.array([x, y, 1.0])
    return u / s, v / s


mask = Image.new("L", photo.size, 0)
d = ImageDraw.Draw(mask)
for x0, y0, x1, y1 in [(590, 752, 995, 852), (1260, 590, 1635, 682)]:
    d.polygon([to_photo(x0, y0), to_photo(x1, y0), to_photo(x1, y1), to_photo(x0, y1)], fill=255)
mask = mask.filter(ImageFilter.GaussianBlur(3))
safe = Image.composite(photo.filter(ImageFilter.GaussianBlur(14)), photo, mask)
safe.crop((0, 0, photo.width, round(photo.width * 5 / 4))).save(A / "real_card_photo_safe.jpg", quality=95)
