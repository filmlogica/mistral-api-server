import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "Mistral API Server is live and ready!", 200

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt", "")
    
    # Simulated response (replace this with actual Mistral generation logic)
    if not prompt:
        return jsonify({"error": "Prompt is missing"}), 400

    generated_text = f"This is a simulated response for prompt: '{prompt}'"
    return jsonify({"response": generated_text})

@app.route("/heartbeat", methods=["GET"])
def heartbeat():
    return jsonify({"status": "alive"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
