from pathlib import Path
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
image = Image.open(ROOT / "inputs" / "sample.jpg").convert("RGB")
arr = np.asarray(image)
gray = np.asarray(image.convert("L"))
channels = [arr[:, :, i] for i in range(3)]

fig, axes = plt.subplots(1, 4, figsize=(13, 4))
axes[0].imshow(arr); axes[0].set_title("RGB image")
for ax, channel, name, cmap in zip(axes[1:], channels, ["Red", "Green", "Blue"], ["Reds", "Greens", "Blues"]):
    ax.imshow(channel, cmap=cmap); ax.set_title(f"{name} channel")
for ax in axes: ax.axis("off")
fig.tight_layout()
out = ROOT / "outputs"
out.mkdir(exist_ok=
fig.savefig(out / "image_representation_channels.png", dpi=150)
Image.fromarray(gray).save(out / "grayscale_image.jpg")
print(f"Dimensions: {image.width} x {image.height}")
print(f"Mode: {image.mode} | Array shape: {arr.shape}")
print(f"Saved visualizations in {out}")
