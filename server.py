from flask import Flask, request, jsonify
import os
import subprocess

app = Flask(__name__)

# Load environment variables
PORT = int(os.getenv("PORT", 11434))
MODEL = os.getenv("MISTRAL_MODEL", "mistral")
OLLAMA_PATH = os.getenv("OLLAMA_PATH", "ollama")
MISTRAL_BACKEND_URL = f"http://0.0.0.0:{PORT}/generate"

@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json()
        prompt = data.get("prompt", "").strip()
        stream = data.get("stream", False)

        if not prompt:
            return jsonify({"error": "No prompt provided."}), 400

        print(f"🧠 Prompt received: {prompt}")

        # Run ollama with subprocess
        result = subprocess.run(
            [OLLAMA_PATH, "run", MODEL, prompt],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            return jsonify({"error": "Ollama execution failed.", "details": result.stderr}), 500

        response_text = result.stdout.strip()
        print(f"✅ Mistral responded:\n{response_text}")
        return jsonify({"response": response_text})

    except Exception as e:
        return jsonify({"error": "Server error", "message": str(e)}), 500

@app.route("/")
def index():
    return jsonify({"message": "Mistral API is running!", "model": MODEL, "port": PORT})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
