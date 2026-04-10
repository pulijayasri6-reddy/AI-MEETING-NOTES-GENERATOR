#  AI Meeting Notes Generator

##  Project Overview
The **AI Meeting Notes Generator** is a Flask-based web application that helps users convert speech into text and generate summaries automatically. It also provides a login system and dashboard to manage meeting records.

##  Features
*  Audio recording (local system)
*  Speech to text conversion
*  Automatic summarization
*  Login authentication
*  Dashboard to view saved meetings
*  JSON-based data storage

##  Technologies Used
* Python
* Flask
* HTML, CSS
* SpeechRecognition
* NumPy, SciPy
* JSON

#  Project Structure & Explanation
ai-meeting-notes/
│
├── speech_to_text.py     # Step 1: Handles audio recording & speech-to-text
├── summarize.py          # Step 2: Generates summary from text
├── app.py                # Step 3: Main Flask application (routes, login, logic)
├── meetings.json         # Step 4: Stores meeting data (text + summary)
├── requirements.txt      # Step 5: Project dependencies
├── README.md             # Step 6: Project documentation
│
├── templates/            # Step 7: HTML pages
│   ├── index.html        # Home page (recording + summary)
│   ├── login.html        # Login page
│   └── dashboard.html    # Dashboard to view meetings
│
├── static/               # Step 8: Static files
│   └── style.css         # Styling for UI
│
└── .gitignore            # Ignore unnecessary files

# File Explanation (Step-by-Step)
##  Step 1: `speech_to_text.py`
* Records audio from microphone (local)
* Converts audio into text using SpeechRecognition
* Contains:
  * `start_recording()`
  * `stop_recording()`
  * `speech_to_text()`
##  Step 2: `summarize.py`
* Takes long text as input
* Splits into sentences
* Returns short summary (first 2 sentences)
##  Step 3: `app.py`
* Main backend using Flask
* Handles:
  * Login system 
  * Recording flow 
  * Summary generation 
  * Dashboard 

##  Step 4: `meetings.json`

* Stores all meeting data
* Format:
  json
{
  "user": "username",
  "text": "full text",
  "summary": "short summary"
}

##  Step 5: `requirements.txt`
* Contains required libraries
* Used for deployment
Example:
Flask
numpy
scipy
SpeechRecognition

##  Step 6: `README.md`

* Documentation of the project
* Explains features, setup, and usage

##  Step 7: `templates/`
### `index.html`
 * Main page
 * Start/Stop recording
 * Show text & summary
### `login.html`
* User login form
### `dashboard.html`
* Displays all saved meetings
##  Step 8: `static/style.css`
* Provides UI design
* Styling for buttons, layout, colors
#  Installation & Setup
bash
git clone https://github.com/your-username/ai-meeting-notes.git
cd ai-meeting-notes
pip install -r requirements.txt
python app.py
# Live Demo
 https://ai-meeting-notes-generator-2.onrender.com
#  Login Credentials
Username: jayasri  
Password: 12345
#  Important Note
* Audio recording works only on local system
* Not supported on cloud platforms like Render
#  Future Enhancements
*  Upload audio file support
*  Advanced AI summarization
*  Database integration
*  Export notes as PDF

#  Author
**Jayasri Puli**

#  Conclusion
This project demonstrates how AI can be used to automate meeting notes by combining speech processing and web development, making it useful for students and professionals.
Just tell 👍
