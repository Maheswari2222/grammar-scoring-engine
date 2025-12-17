import sounddevice as sd
import soundfile as sf

duration = 5  # seconds
fs = 44100

print("Recording...")
audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()
sf.write("uploads/input.wav", audio, fs)
print("Saved as uploads/input.wav")
