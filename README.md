
# Grammar Scoring Engine from Voice Samples

## Overview

This project is a web application that analyzes spoken English audio and provides a grammar score based on the transcribed text.  
It uses:

- **OpenAI Whisper** for automatic speech recognition (ASR)  
- **LanguageTool** for grammar checking  
- **Flask** as the web framework  

Users upload audio files, and the app returns the spoken text, grammar errors, and a simple grammar score.

---

## Features

- Upload voice samples (`.wav` format) via the web interface  
- Speech-to-text transcription with Whisper  
- Grammar checking using LanguageTool  
- Detailed grammar error messages with suggestions  
- Grammar score calculation (score out of 10)  

---

## Requirements

- Python 3.7+  
- FFmpeg installed and added to system PATH (required by Whisper)  
- Required Python packages (listed in `requirements.txt`)  

---

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/grammar-scoring-engine.git
cd grammar-scoring-engine
```

### 2. Create and activate a virtual environment (recommended)

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install FFmpeg

- Download FFmpeg from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)  
- Add FFmpeg `bin` folder to your system PATH environment variable  
- Verify installation with:

```bash
ffmpeg -version
```

---

## Running the Application Locally

```bash
python app.py
```

Open your browser at:  
[http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Using the Application

1. Click **Choose File** and upload a `.wav` audio file with spoken English  
2. Submit the form  
3. View the transcribed text, grammar score, and detailed grammar errors  

---

## Deployment

You can deploy this Flask app with Whisper and LanguageTool to the cloud.

### Recommended Hosting: [Render.com](https://render.com)

1. Push your code to GitHub  
2. Create a new web service on Render linked to your repo  
3. Set build command: `pip install -r requirements.txt`  
4. Set start command: `gunicorn app:app`  
5. Deploy and get your live URL  

**Note:** Ensure FFmpeg is available on the server (Render supports it by default).

---

## Limitations

- Microphone input directly from browser is NOT supported  
- Long audio files may cause timeouts  
- Running on free-tier cloud plans may have resource limits  

---

## Troubleshooting

- If you see errors about missing FFmpeg, verify it is installed and in PATH  
- If `language_tool_python` gives errors, ensure Java Runtime Environment (JRE) is installed  
- Use short audio clips for faster processing  

---

## Dependencies

- Flask  
- OpenAI Whisper (`whisper` Python package)  
- LanguageTool Python wrapper (`language_tool_python`)  
- PyTorch (required by Whisper)  
- FFmpeg (external system dependency)  

---

## License

This project is licensed under the MIT License.

---

## Acknowledgements

- OpenAI Whisper: https://github.com/openai/whisper  
- LanguageTool: https://languagetool.org/  
- Flask: https://flask.palletsprojects.com/

---

## Contact

For any questions or support, please contact:  
**Your Name** — your.email@example.com
