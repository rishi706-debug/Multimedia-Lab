from pathlib import Path
from PIL import Image
import json

root = Path(__file__).resolve().parents[1]
source = root / "inputs" / "sample.jpg"
with Image.open(source) as img:
    report = {
        "file": source.name, "format": img.format, "mode": img.mode,
        "width": img.width, "height": img.height,
        "file_size_bytes": source.stat().st_size,
        "aspect_ratio": round(img.width / img.height, 3)
    }
out = root / "outputs"
out.mkdir(exist_ok=True)
(out / "image_metadata_report.json").write_text(json.dumps(report, indent=2))
print(json.dumps(report, indent=2))
