from pathlib import Path
import cv2
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / "inputs" / "sample.jpg"
out = ROOT / "outputs"
out.mkdir(exist_ok=True)

image = cv2.imread(str(source))
if image is None:
    raise FileNotFoundError(source)

brightness_contrast = cv2.convertScaleAbs(image, alpha=1.25, beta=25)
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
l, a, b = cv2.split(lab)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
enhanced_lab = cv2.merge((clahe.apply(l), a, b))
clahe_image = cv2.cvtColor(enhanced_lab, cv2.COLOR_LAB2BGR)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
equalized = cv2.equalizeHist(gray)
kernel = __import__("numpy").array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
sharpened = cv2.filter2D(image, -1, kernel)

cv2.imwrite(str(out / "brightness_contrast.jpg"), brightness_contrast)
cv2.imwrite(str(out / "clahe_enhanced.jpg"), clahe_image)
cv2.imwrite(str(out / "histogram_equalized.jpg"), equalized)
cv2.imwrite(str(out / "sharpened_image.jpg"), sharpened)
cv2.imwrite(str(out / "final_enhanced_image.jpg"), clahe_image)

comparison = cv2.cvtColor(cv2.hconcat([image, clahe_image]), cv2.COLOR_BGR2RGB)
plt.figure(figsize=(12, 5))
plt.imshow(comparison)
plt.title("Original image | CLAHE enhanced image")
plt.axis("off")
plt.tight_layout()
plt.savefig(out / "before_after_comparison.jpg", dpi=150)
print(f"Enhancement outputs saved to: {out}")
