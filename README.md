Grammar Scoring Engine from Voice Samples
Project Overview

The Grammar Scoring Engine from Voice Samples is an AI-based web application that evaluates the grammatical correctness of spoken English. The system takes voice input from users, converts it into text using automatic speech recognition, analyzes grammatical errors using natural language processing techniques, and generates a grammar score along with corrective feedback.

This project is suitable for final-year engineering projects, internships, and educational demonstrations.

Objectives

Convert spoken English into text

Identify grammatical errors in spoken sentences

Generate a grammar score based on detected errors

Provide corrective suggestions for improvement

Build a user-friendly web interface for audio upload

System Architecture
Voice Input (.wav)
        |
Speech-to-Text (Whisper ASR)
        |
Grammar Analysis (LanguageTool NLP)
        |
Scoring Logic
        |
Grammar Score and Feedback

Technology Stack
Component	Technology
Programming Language	Python 3.10
Web Framework	Flask
Speech Recognition	OpenAI Whisper
Grammar Checking	LanguageTool
Audio Processing	FFmpeg
Frontend	HTML, JavaScript
Backend	Flask REST API
Operating System	Windows
Project Structure
grammar_scoring_engine/
│
├── app.py
├── record_audio.py (optional)
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── uploads/
│   └── input.wav

Installation and Setup
Step 1: Clone or Download the Project
git clone <repository-url>
cd grammar_scoring_engine

Step 2: Create Virtual Environment (Optional but Recommended)
python -m venv venv
venv\Scripts\activate

Step 3: Install Required Libraries
pip install -r requirements.txt

Step 4: Install FFmpeg

Download FFmpeg from:
https://www.gyan.dev/ffmpeg/builds/

Extract and move the folder to:

C:\ffmpeg


Ensure the following file exists:

C:\ffmpeg\bin\ffmpeg.exe


Note: FFmpeg path is injected at runtime inside app.py.

How to Run the Project
python app.py


Open a browser and navigate to:

http://127.0.0.1:5000


Upload a .wav audio file and click Analyze.

Sample Output
{
  "spoken_text": "I am go to college yesterday",
  "grammar_score": 6,
  "error_count": 2,
  "errors": [
    {
      "message": "Incorrect verb tense",
      "suggestions": ["went"]
    }
  ]
}

Grammar Scoring Method

Maximum score: 10

Each grammatical error reduces the score

Formula:

Grammar Score = 10 − (Number of Errors × 2)

Use Cases

Spoken English learning applications

Interview practice systems

Language proficiency assessment tools

Voice-based educational platforms

AI-powered learning assistants

Advantages

Fully automated grammar evaluation

Works with real voice input

CPU-based execution (no GPU required)

Easy to extend with additional scoring metrics

Future Enhancements

Fluency and pronunciation scoring

CEFR level classification (A1–C1)

Text-to-speech feedback

Android mobile application

Multilingual support

Academic Relevance

This project demonstrates concepts from:

Artificial Intelligence

Natural Language Processing

Speech Recognition

Web Application Development

Human Computer Interaction

Project Category

Artificial Intelligence / Machine Learning / NLP

License

This project is developed for educational and academic purposes.

Acknowledgements

OpenAI Whisper

LanguageTool

Flask Framework

FFmpeg

If you want, I can now provide:

Project Report (DOC/PDF)

PPT for Viva

Resume-ready project description

Viva questions and answers

Just tell me what you need next.

