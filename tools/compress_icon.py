from PIL import Image
from pathlib import Path

targets = [
    Path(r"C:\Users\Kompukter\Documents\GitHub\Voxy- Neoforged\src\main\resources\assets\voxy\icon.png"),
    Path(r"C:\Users\Kompukter\Documents\GitHub\Voxy- Neoforged\voxy-reborn-icon.png"),
]

src = targets[0]
img = Image.open(src).convert("RGBA")
print(f"original: {img.size} {src.stat().st_size / 1024:.0f} KB")

out = img.resize((256, 256), Image.Resampling.LANCZOS)

# Quantize RGB for smaller PNG; keep alpha channel
r, g, b, a = out.split()
rgb = Image.merge("RGB", (r, g, b))
pal = rgb.quantize(colors=96, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.FLOYDSTEINBERG)
rgba = pal.convert("RGBA")
rgba.putalpha(a)

for path in targets:
    path.parent.mkdir(parents=True, exist_ok=True)
    rgba.save(path, format="PNG", optimize=True, compress_level=9)
    im = Image.open(path)
    print(f"FINAL {im.size} {path.stat().st_size / 1024:.1f} KB  {path}")

# If still over ~150KB, try 128px fallback for loader icon
if targets[0].stat().st_size > 150_000:
    small = rgba.resize((128, 128), Image.Resampling.LANCZOS)
    for path in targets:
        small.save(path, format="PNG", optimize=True, compress_level=9)
        print(f"128px {path.stat().st_size / 1024:.1f} KB  {path.name}")
