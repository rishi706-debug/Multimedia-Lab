# Multimedia and Image Processing

**Student ID:** IC-2K22-68  
**Name:** Rishi Raghuwanshi

A Python project containing two practical clusters:

## Cluster 01 — Multimedia Fundamentals
- Audio sampling and quantization (`basic/audio_sampling.py`)
- Image representation and color channels (`basic/image_representation.py`)
- Video frame extraction (`basic/video_frame_extraction.py`)
- Image, audio and video metadata reports (`metadata_analyzer/`)

## Cluster 02 — Image Processing
- Brightness and contrast adjustment
- Histogram equalization and CLAHE
- Sharpening and before/after comparison (`image_enhancement/image_enhancement.py`)

## Setup
```bash
python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
```

## Run examples
Run commands from the project root:
```bash
python Cluster01-Multimedia-Fundamentals/basic/audio_sampling.py
python Cluster01-Multimedia-Fundamentals/basic/image_representation.py
python Cluster01-Multimedia-Fundamentals/metadata_analyzer/image_metadata_analyzer.py
python Cluster02-Image-Processing/image_enhancement/image_enhancement.py
```
For video extraction, provide a video file:
```bash
python Cluster01-Multimedia-Fundamentals/basic/video_frame_extraction.py path/to/video.mp4
```

Generated reports and images are saved in each cluster's `outputs/` directory.
Sample files are provided in `inputs/`. This project is intended for learning and experimentation.
