from pathlib import Path
import argparse
import cv2

parser = argparse.ArgumentParser(description="Extract sample frames from a video.")
parser.add_argument("video", help="Path to input video")
args = parser.parse_args()
video = Path(args.video)
if not video.exists():
    raise FileNotFoundError(video)

cap = cv2.VideoCapture(str(video))
if not cap.isOpened():
    raise RuntimeError("Could not open video file")
fps = cap.get(cv2.CAP_PROP_FPS)
total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
out = Path(__file__).resolve().parents[1] / "outputs"
out.mkdir(exist_ok=True)
count = 0
for fraction in (0.1, 0.3, 0.5, 0.7, 0.9):
    cap.set(cv2.CAP_PROP_POS_FRAMES, min(total - 1, int(total * fraction)))
    ok, frame = cap.read()
    if ok:
        target = out / f"frame_{count + 1}.jpg"
        cv2.imwrite(str(target), frame)
        count += 1
cap.release()
print(f"FPS: {fps:.2f} | Total frames: {total} | Extracted: {count}")
