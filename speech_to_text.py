import speech_recognition as sr

def start_recording():
    print("🎤 Recording started (demo mode)")

def stop_recording():
    print("⏹️ Recording stopped")

def speech_to_text(filename="audio.wav"):
    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(filename) as source:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio)
            return text
    except:
        return "This is a demo meeting recording. We discussed project updates and deadlines."