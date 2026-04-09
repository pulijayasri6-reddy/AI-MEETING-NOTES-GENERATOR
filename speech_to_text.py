import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import speech_recognition as sr

fs = 44100
recording = []
stream = None

def callback(indata, frames, time, status):
    global recording
    recording.append(indata.copy())

# ✅ Start recording
def start_recording():
    global stream, recording
    recording = []

    stream = sd.InputStream(samplerate=fs, channels=1, dtype='int16', callback=callback)
    stream.start()

    print("🎤 Recording started...")

# ✅ Stop recording
def stop_recording(filename="audio.wav"):
    global stream, recording

    stream.stop()
    stream.close()

    audio_data = np.concatenate(recording, axis=0)
    write(filename, fs, audio_data)

    print("✅ Recording saved")

# ✅ Convert speech to text (IMPORTANT)
def speech_to_text(filename="audio.wav"):
    recognizer = sr.Recognizer()

    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio)
        print("📝 You said:", text)
        return text
    except Exception as e:
        print("❌ Error:", e)
        return ""