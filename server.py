from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get("prompt", "")

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )
    if response.ok:
        return jsonify(response.json())
    else:
        return jsonify({"error": response.text}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=11434)
