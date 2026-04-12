# 🎤 AI Meeting Notes Generator
## 📌 Project Overview
AI Meeting Notes Generator is a web application that allows users to:
* Record meeting audio (demo mode)
* Convert speech to text
* Generate a short summary
* Store and view past meeting notes

## 🚀 Features
* 🔐 User Authentication (Login & Signup)
* 🎤 Start & Stop Recording (Demo Mode)
* 📝 Speech-to-Text Conversion
* 📌 Automatic Text Summarization
* 📊 Dashboard to view previous meetings
* 💾 Data stored in JSON files

## 🛠️ Technologies Used
* Python 🐍
* Flask 🌐
* HTML, CSS 🎨
* JSON (for data storage)

## 📂 Project Structure
AI-MEETING-NOTES-GENERATOR/
│
├── app.py
├── speech_to_text.py
├── summarize.py
├── users.json
├── meetings.json
│
├── templates/
│   ├── login.html
│   ├── signup.html
│   ├── index.html
│   └── dashboard.html
│
├── static/
│   └── style.css
│
└── README.md

##  How It Works
### 1️ User Authentication
* Users can sign up and log in
* Data is stored in `users.json`

### 2️ Recording (Demo Mode)
* Click **Start Recording**
* Click **Stop & Summarize**
* System simulates recording and generates text

### 3️ Speech-to-Text
* Uses `speech_recognition` library
* Converts audio (or demo input) into text
  
### 4️ Summarization
* First 2 sentences are extracted as summary

### 5️ Dashboard
* Stores meeting data in `meetings.json`
* Displays all previous meetings

##  How to Run the Project
### Step 1: Install dependencies
pip install flask speechrecognition
### Step 2: Run the app
python app.py
### Step 3: Open browser
http://127.0.0.1:5000/

##  Important Note
* Recording is currently in **demo mode**
* Real microphone recording is not implemented yet
##  Future Improvements
*  Real-time microphone recording
*  Cloud deployment (Render)
*  Mobile responsive UI
*  Password encryption
*  Advanced AI summarization

##  Author
**Jayasri Puli**
##  Conclusion
This project demonstrates how to build a simple AI-based web application using Flask, including authentication, data storage, and text processing.

---
