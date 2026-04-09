from flask import Flask, render_template
from speech_to_text import start_recording, stop_recording, speech_to_text
from summarize import summarize_text
import json, os

app = Flask(__name__)

DATA_FILE = "meetings.json"

# Load data
def load_meetings():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# Save data
def save_meetings(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/start")
def start():
    start_recording()
    return render_template("index.html", message="🎤 Recording started...")


@app.route("/stop")
def stop():
    stop_recording()
    text = speech_to_text()
    summary = summarize_text(text)

    # Save data
    meetings = load_meetings()
    meetings.append({
        "text": text,
        "summary": summary
    })
    save_meetings(meetings)

    return render_template("index.html", text=text, summary=summary)


@app.route("/dashboard")
def dashboard():
    meetings = load_meetings()
    return render_template("dashboard.html", meetings=meetings)


if __name__ == "__main__":
    app.run(debug=True)