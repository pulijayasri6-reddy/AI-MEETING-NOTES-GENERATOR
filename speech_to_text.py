import speech_recognition as sr

# ✅ Start recording (disabled for server)
def start_recording():
    print("⚠️ Recording not supported on server")

# ✅ Stop recording (disabled)
def stop_recording(filename="audio.wav"):
    print("⚠️ Stop recording (not available)")

# ✅ Convert speech to text (demo or file-based)
def speech_to_text(filename="audio.wav"):
    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(filename) as source:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio)
            print("📝 You said:", text)
            return text
    except:
        return "Demo text: This is a sample meeting transcription."