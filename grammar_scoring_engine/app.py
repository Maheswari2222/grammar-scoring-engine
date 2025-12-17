import os

# 🔴 IMPORTANT: Force FFmpeg path for Whisper (Windows fix)
os.environ["PATH"] += os.pathsep + r"C:\ffmpeg\bin"

from flask import Flask, request, jsonify, render_template
import whisper
import language_tool_python

# Flask app setup
app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load models ONCE at startup
print("Loading Whisper model...")
asr_model = whisper.load_model("base")

print("Loading Grammar Tool...")
grammar_tool = language_tool_python.LanguageTool('en-US')

# Home route
@app.route("/")
def index():
    return render_template("index.html")

# Audio analysis route
@app.route("/analyze", methods=["POST"])
def analyze_audio():
    try:
        # Check audio file
        if "audio" not in request.files:
            return jsonify({"error": "No audio file uploaded"}), 400

        audio_file = request.files["audio"]
        audio_path = os.path.join(UPLOAD_FOLDER, "input.wav")
        audio_file.save(audio_path)

        # 🎙️ Speech to Text
        result = asr_model.transcribe(audio_path)
        spoken_text = result.get("text", "").strip()

        if not spoken_text:
            return jsonify({"error": "Could not recognize speech"}), 400

        # 🧠 Grammar Checking
        matches = grammar_tool.check(spoken_text)

        errors = []
        for match in matches:
            errors.append({
                "message": match.message,
                "suggestions": match.replacements
            })

        # 📊 Grammar Score Logic
        error_count = len(matches)
        grammar_score = max(0, 10 - error_count * 2)

        # ✅ Final Response
        return jsonify({
            "spoken_text": spoken_text,
            "grammar_score": grammar_score,
            "error_count": error_count,
            "errors": errors
        })

    except Exception as e:
        # 🔥 Prevent Flask 500 crash
        return jsonify({
            "error": "Processing failed",
            "details": str(e)
        }), 500

# Run app
if __name__ == "__main__":
    app.run(debug=True)
