#  AI Meeting Notes Generator

##  Project Overview
AI Meeting Notes Generator is a Flask-based web application that records audio, converts speech to text, and generates a short summary automatically. It helps users save time by converting meeting discussions into structured notes.

##  Features
*  Audio Recording
*  Speech to Text Conversion
*  Automatic Text Summarization
*  User Login System
*  Dashboard to View Previous Meetings
*  Data Storage using JSON

## Technologies Used
* Python
* Flask
* HTML, CSS
* SpeechRecognition
* SoundDevice
* NumPy
* JSON

##  Project Structure
ai-meeting-notes/
│
├── app.py
├── speech_to_text.py
├── summarize.py
├── meetings.json
│
├── templates/
│   ├── login.html
│   ├── index.html
│   └── dashboard.html
│
├── static/
│   └── style.css
│
└── README.md

##  Installation & Setup
### 1️ Clone the Repository
git clone https://github.com/your-username/ai-meeting-notes.git
cd ai-meeting-notes

### 2️ Install Dependencies
pip install flask sounddevice numpy scipy SpeechRecognition

### 3️ Run the Application
python app.py

### 4️ Open in Browser
http://127.0.0.1:5000/

##  Login Details
Username: jayasri  
Password: 12345

##  How It Works
1. User logs in
2. Clicks **Start Recording**
3. Speaks into microphone
4. Clicks **Stop & Summarize**
5. App:
   * Saves audio
   * Converts speech to text
   * Generates summary
6. Data stored in `meetings.json`
7. View results in Dashboard

##  Future Enhancements
*  Advanced AI summarization
*  Database integration (MySQL)
*  Export notes as PDF
*  Multi-user authentication system
*  Improved UI design

##  Contributing
Feel free to fork this project and submit pull requests.

##  License
This project is for educational purposes.

##  Author
**Jayasri Puli**
