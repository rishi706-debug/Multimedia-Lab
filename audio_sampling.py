from pathlib import Path
import wave
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "inputs" / "sample.wav"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

with wave.open(str(INPUT), "rb") as wav:
    rate, frames = wav.getframerate(), wav.getnframes()
    samples = np.frombuffer(wav.readframes(frames), dtype=np.int16)

time = np.arange(len(samples)) / rate
# Demonstrate lower-rate sampling by selecting every 4th sample.
reduced = samples[::4]
quantized = (np.round(reduced / 2048) * 2048).astype(np.int16)

fig, axes = plt.subplots(2, 1, figsize=(10, 6))
axes[0].plot(time[:min(2000, len(time))], samples[:2000])
axes[0].set_title("Original audio waveform")
axes[1].plot(np.arange(min(500, len(reduced))) / (rate / 4), reduced[:500], label="Sampled")
axes[1].step(np.arange(min(500, len(quantized))) / (rate / 4), quantized[:500],
             where="mid", label="Quantized", alpha=.7)
axes[1].legend()
for ax in axes: ax.set_xlabel("Time (seconds)")
fig.tight_layout()
fig.savefig(OUT / "audio_sampling_quantization.png", dpi=150)
print(f"Sample rate: {rate} Hz | Samples: {len(samples)}")
print(f"Saved: {OUT / 'audio_sampling_quantization.png'}")
