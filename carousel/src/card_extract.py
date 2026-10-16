"""Rectify the real APEC card from the user's photo (perspective warp)."""
import numpy as np
from PIL import Image
from pathlib import Path

A = Path(__file__).resolve().parent.parent / "assets"
W, H = 1712, 1080                      # ID-1 card ratio 85.6 x 54 mm
# card corners in the photo: TL, TR, BR, BL
SRC = [(555, 1928), (1274, 1774), (1352, 2226), (617, 2392)]
DST = [(0, 0), (W, 0), (W, H), (0, H)]


def coeffs(dst, src):
    m = []
    for (x, y), (u, v) in zip(dst, src):
        m.append([x, y, 1, 0, 0, 0, -u * x, -u * y])
        m.append([0, 0, 0, x, y, 1, -v * x, -v * y])
    b = np.array(src).reshape(8)
    return np.linalg.solve(np.array(m, float), b)


photo = Image.open(A / "real_card_photo.jpg").convert("RGB")
flat = photo.transform((W, H), Image.PERSPECTIVE, coeffs(DST, SRC), Image.BICUBIC)
flat.save(A / "real_card_flat_raw.png")
