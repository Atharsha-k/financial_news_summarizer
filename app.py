from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Financial News Summarizer Running!"

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.json
    text = data.get("text", "")

    # Replace with your logic
    summary = text[:100]

    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)