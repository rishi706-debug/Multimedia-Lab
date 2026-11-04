from pathlib import Path
import wave, json

root = Path(__file__).resolve().parents[1]
source = root / "inputs" / "sample.wav"
with wave.open(str(source), "rb") as wav:
    report = {
        "file": source.name, "channels": wav.getnchannels(),
        "sample_width_bytes": wav.getsampwidth(),
        "sample_rate_hz": wav.getframerate(),
        "total_frames": wav.getnframes(),
        "duration_seconds": round(wav.getnframes() / wav.getframerate(), 3)
    }
out = root / "outputs"
out.mkdir(exist_ok=True)
(out / "audio_metadata_report.json").write_text(json.dumps(report, indent=2))
print(json.dumps(report, indent=2))
