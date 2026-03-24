from flask import Flask, request, jsonify
from summarizer import summarize_text
import nltk

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)

@app.route("/")
def home():
    return "Financial News Summarizer is Running!"

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.json
    text = data.get("text", "")

    if not text.strip():
        return jsonify({"error": "Please enter some text!"})

    summary = summarize_text(text, 3)

    return jsonify({"summary": summary})

# Important for Render
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)