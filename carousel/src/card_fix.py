"""Repair the thumb-covered corner of the rectified real APEC card, round corners,
and soften the document number and date of birth before publishing."""
import numpy as np
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

A = Path(__file__).resolve().parent.parent / "assets"
card = Image.open(A / "real_card_flat_raw.png").convert("RGB")
W, H = card.size
arr = np.asarray(card).astype(float)

# 1) thumb mask traced on the rectified card (x of the thumb edge per y)
edge = [(0, 116), (40, 132), (80, 138), (120, 138), (160, 133), (200, 127), (240, 119),
        (280, 110), (320, 92), (360, 66), (395, 34), (412, 0)]
poly = [(0, 0)] + [(x, y) for y, x in edge]
m = Image.new("L", (W, H), 0)
ImageDraw.Draw(m).polygon(poly, fill=255)
mask = np.asarray(m.filter(ImageFilter.MaxFilter(13))) > 0

# 2) rebuild the guilloche background from letter-free rows, shifted right by DX
DX = 150
band = list(range(146, 176))
band = band + band[::-1]                      # mirror-tile to hide seams
fill = arr.copy()
for y in range(0, 425):
    if 133 <= y <= 175 or y >= 259:
        src_y = y
    else:
        src_y = band[y % len(band)]
    fill[y, :W - DX] = arr[src_y, DX:]
img = Image.fromarray(np.where(mask[..., None], fill, arr).astype(np.uint8))


# 3) redraw hidden letters, fitted to the visible ones
def fit(font_path, word, tail, tail_x0, tail_x1, top, size_guess):
    """Find font size so that `tail` spans tail_x0..tail_x1; return font and x/y offset of `word`."""
    for s in range(size_guess - 40, size_guess + 60):
        f = ImageFont.truetype(font_path, s)
        w_tail = f.getlength(tail)
        if w_tail >= tail_x1 - tail_x0:
            break
    x_word = tail_x0 - f.getlength(word[: len(word) - len(tail)])
    bbox = f.getbbox(word)
    return f, x_word, top - bbox[1]


red = (204, 32, 22)
d = ImageDraw.Draw(img)
# "A": match the cap height of the visible "PEC" (rows 22..120) and end just before "P"
f1 = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSansBold.ttf", 134)
ab = f1.getbbox("A")
x1, y1 = 186 - ab[2], 22 - ab[1]
d.text((x1, y1), "A", font=f1, fill=red)
f2, x2, y2 = fit("/usr/share/fonts/truetype/freefont/FreeSerifItalic.ttf", "Russia", "ussia", 122, 306, 176, 80)
d.text((x2, y2), "R", font=f2, fill=(196, 38, 40))
print("A at", round(x1), round(y1), f1.size, "| R at", round(x2), round(y2), f2.size)

soft = Image.fromarray((mask * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(3))
img = Image.composite(img.filter(ImageFilter.GaussianBlur(1.1)), card, soft)

# 4) soften document number and date of birth (public post)
for box in [(596, 760, 985, 846), (1266, 596, 1625, 676)]:
    img.paste(img.crop(box).filter(ImageFilter.GaussianBlur(14)), box[:2])

# 5) rounded corners
alpha = Image.new("L", (W, H), 0)
ImageDraw.Draw(alpha).rounded_rectangle((0, 0, W - 1, H - 1), radius=68, fill=255)
img.putalpha(alpha)
img.save(A / "real_card_flat.png")
