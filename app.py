from flask import Flask, render_template, request, redirect, url_for, session
from speech_to_text import start_recording, stop_recording, speech_to_text
from summarize import summarize_text
import json, os

app = Flask(__name__)
app.secret_key = "your_secret_key"  # for session management

DATA_FILE = "meetings.json"

# Temporary users (replace with database for production)
users = {"jayasri": "12345"}  # username: password

# ---------------- Login Page ---------------- #
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users and users[username] == password:
            session["username"] = username
            return redirect(url_for("home"))
        else:
            return render_template("login.html", error="Invalid username or password")
    return render_template("login.html")

# ---------------- Home Page (Recording / Summarize) ---------------- #
@app.route("/home")
def home():
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template("index.html")

# ---------------- Logout ---------------- #
@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))

# ---------------- Start Recording ---------------- #
@app.route("/start")
def start():
    if "username" not in session:
        return redirect(url_for("login"))
    start_recording()
    return render_template("index.html", message="🎤 Recording started...")

# ---------------- Stop Recording & Summarize ---------------- #
@app.route("/stop")
def stop():
    if "username" not in session:
        return redirect(url_for("login"))
    stop_recording()
    text = speech_to_text()
    summary = summarize_text(text)

    # Save to meetings.json
    meetings = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            meetings = json.load(f)
    meetings.append({
        "user": session["username"],
        "text": text,
        "summary": summary
    })
    with open(DATA_FILE, "w") as f:
        json.dump(meetings, f, indent=4)

    return render_template("index.html", text=text, summary=summary)

# ---------------- Dashboard ---------------- #
@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        return redirect(url_for("login"))
    meetings = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            meetings = json.load(f)
    return render_template("dashboard.html", meetings=meetings)

if __name__ == "__main__":
    app.run(debug=True)