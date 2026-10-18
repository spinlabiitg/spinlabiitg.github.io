"""Favicon set in the SPIN identity: white rounded bars (the waveform mark from
spin_branding/qr/make_qr.py) on a rounded square with the indigo -> deep-teal gradient.

16 px uses 3 bars and 32/48 px use 5, snapped to whole pixels so tab icons stay crisp
(no SVG favicon: browsers prefer it and it blurs at 16 px). App icons use the full 9-bar mark.
Run from the site root:  python scripts/make_favicon.py
Writes: favicon.ico, images/favicon-32.png, images/apple-touch-icon.png, images/icon-512.png
"""
from PIL import Image, ImageDraw

C0, C1 = (30, 58, 138), (13, 110, 110)          # same as the QR / poster identity
MARK9 = [0.2, 0.4, 0.7, 1.0, 0.7, 0.45, 0.8, 0.5, 0.25]
MARK5 = [0.42, 0.78, 1.0, 0.55, 0.3]
MARK3 = [0.6, 1.0, 0.7]                       # 16 px tab icon: 2 px bars on whole pixels


def hexc(c):
    return "#%02x%02x%02x" % c


def bar_layout(heights, size, pad, gap_ratio):
    n = len(heights)
    inner = size - 2 * pad
    bw = inner / (n + (n - 1) * gap_ratio)
    gap = bw * gap_ratio
    out = []
    for i, h in enumerate(heights):
        x = pad + i * (bw + gap)
        bh = max(bw, h * inner)
        y = (size - bh) / 2
        out.append((x, y, bw, bh))
    return out


def render(size, heights, pad_frac, gap_ratio, radius_frac=0.22, ss=8, snap=False):
    S = size * ss
    grad = Image.new("RGB", (S, S))
    px = grad.load()
    for y in range(S):
        for x in range(S):
            t = (x + y) / (2 * (S - 1))           # diagonal gradient, top-left -> bottom-right
            px[x, y] = tuple(round(C0[k] + (C1[k] - C0[k]) * t) for k in range(3))
    mask = Image.new("L", (S, S), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, S - 1, S - 1], radius=round(S * radius_frac), fill=255)
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    img.paste(grad, (0, 0), mask)
    d = ImageDraw.Draw(img)
    if snap:  # lay bars out on the real pixel grid so small icons stay sharp
        bars = [(round(x) * ss, round(y) * ss, max(1, round(w)) * ss, round(h) * ss)
                for x, y, w, h in bar_layout(heights, size, size * pad_frac, gap_ratio)]
    else:
        bars = bar_layout(heights, S, S * pad_frac, gap_ratio)
    for x, y, w, h in bars:
        d.rounded_rectangle([x, y, x + w, y + h], radius=w / 2, fill=(255, 255, 255, 255))
    return img.resize((size, size), Image.LANCZOS)


if __name__ == "__main__":
    small = [render(16, MARK3, 3 / 16, 1.0, snap=True)] + [render(n, MARK5, 0.2, 0.55, snap=True) for n in (32, 48)]
    small[2].save("favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)], append_images=small[:2])
    small[1].save("images/favicon-32.png")
    render(180, MARK9, 0.2, 0.6, radius_frac=0.0).convert("RGB").save("images/apple-touch-icon.png")  # iOS rounds it
    render(512, MARK9, 0.2, 0.6).save("images/icon-512.png")
    print("favicons written")
