from pathlib import Path
import cv2, json, argparse

parser = argparse.ArgumentParser(description="Read basic video metadata.")
parser.add_argument("video", help="Path to video")
args = parser.parse_args()
path = Path(args.video)
cap = cv2.VideoCapture(str(path))
if not cap.isOpened():
    raise RuntimeError(f"Could not open {path}")
fps = cap.get(cv2.CAP_PROP_FPS)
frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
report = {
    "file": path.name, "width": int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
    "height": int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
    "fps": round(fps, 3), "frame_count": frames,
    "duration_seconds": round(frames / fps, 3) if fps else None
}
cap.release()
out = Path(__file__).resolve().parents[1] / "outputs"
out.mkdir(exist_ok=True)
(out / "video_metadata_report.json").write_text(json.dumps(report, indent=2))
print(json.dumps(report, indent=2))
