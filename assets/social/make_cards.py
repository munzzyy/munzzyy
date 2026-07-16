#!/usr/bin/env python3
"""Build 1280x640 social preview cards in the portfolio palette."""
import os
import sys

from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 640
LEFT = 96
MAXW = 1064
BG = (13, 17, 23)
TITLE = (230, 237, 243)
SUB = (201, 209, 217)
URLC = (139, 148, 158)
SANS_BOLD = "/usr/share/fonts/liberation/LiberationSans-Bold.ttf"
SANS = "/usr/share/fonts/liberation/LiberationSans-Regular.ttf"
MONO = "/usr/share/fonts/liberation/LiberationMono-Regular.ttf"
HERE = os.path.dirname(os.path.abspath(__file__))


def tint(accent, a=0.10):
    return tuple(int(b + a * (c - b)) for b, c in zip(BG, accent))


def star(d, color):
    import math
    cx, cy, r1, r2 = 1080, 300, 190, 78
    pts = []
    for i in range(10):
        r = r1 if i % 2 == 0 else r2
        ang = math.pi / 2 + i * math.pi / 5
        pts.append((cx + r * math.cos(ang), cy - r * math.sin(ang)))
    d.line(pts + [pts[0]], fill=color, width=20, joint="curve")


def prompt(d, color):
    d.line([(950, 190), (1130, 300), (950, 410)], fill=color, width=26, joint="curve")
    d.line([(1168, 398), (1262, 398)], fill=color, width=26)


CARDS = {
    "awesome-webmcp": {
        "accent": (163, 113, 247),
        "pitch": "The curated list for WebMCP. Specs, SDKs, demos, and working code.",
        "motif": star,
    },
    "munzzyy": {
        "accent": (88, 166, 255),
        "pitch": "Open-source tools and upstream fixes where correctness matters.",
        "motif": prompt,
    },
}


def fit_title(name):
    size = 146
    f = ImageFont.truetype(SANS_BOLD, size)
    while f.getbbox(name)[2] - f.getbbox(name)[0] > MAXW and size > 80:
        size -= 2
        f = ImageFont.truetype(SANS_BOLD, size)
    return f


def wrap(text, f, maxw):
    lines, cur = [], ""
    for word in text.split():
        cand = (cur + " " + word).strip()
        if f.getbbox(cand)[2] - f.getbbox(cand)[0] <= maxw or not cur:
            cur = cand
        else:
            lines.append(cur)
            cur = word
    lines.append(cur)
    return lines


def card(name, spec):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    spec["motif"](d, tint(spec["accent"]))
    d.ellipse((1178, 90, 1190, 102), fill=spec["accent"])
    f = fit_title(name)
    d.text((LEFT, 217 - f.getbbox(name)[1]), name, font=f, fill=TITLE)
    d.rectangle((LEFT, 362, 180, 369), fill=spec["accent"])
    fs = ImageFont.truetype(SANS, 40)
    for i, line in enumerate(wrap(spec["pitch"], fs, MAXW)[:2]):
        d.text((LEFT, 416 + 60 * i - fs.getbbox("X")[1]), line, font=fs, fill=SUB)
    fm = ImageFont.truetype(MONO, 28)
    url = f"github.com/munzzyy/{name}"
    d.text((LEFT, 522 - fm.getbbox(url)[1]), url, font=fm, fill=URLC)
    out = os.path.join(HERE, f"{name}.png")
    im.save(out)
    print(out)


def main():
    names = sys.argv[1:] or list(CARDS)
    for name in names:
        card(name, CARDS[name])


if __name__ == "__main__":
    main()
