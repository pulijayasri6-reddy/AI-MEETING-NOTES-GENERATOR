from flask import Flask, render_template, request, redirect, url_for, session
import json, os

app = Flask(__name__)
app.secret_key = "your_secret_key"

USERS_FILE = "users.json"

# ---------------- Load Users ---------------- #
def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    return {}

# ---------------- Save Users ---------------- #
def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

# ---------------- Login ---------------- #
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        users = load_users()

        if username in users and users[username] == password:
            session["username"] = username
            return redirect(url_for("home"))
        else:
            return render_template("login.html", error="Invalid username or password")

    return render_template("login.html")

# ---------------- Signup ---------------- #
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        users = load_users()

        if username in users:
            return render_template("signup.html", error="User already exists")

        users[username] = password
        save_users(users)

        return redirect(url_for("login"))

    return render_template("signup.html")

# ---------------- Home ---------------- #
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

if __name__ == "__main__":
    app.run(debug=True)