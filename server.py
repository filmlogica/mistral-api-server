from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "status": "✅ IdeaReactor server is running!",
        "message": "Welcome to the API layer of IdeaReactor powered by Mistral and Shopify."
    }), 200

@app.route('/heartbeat', methods=['GET'])
def heartbeat():
    return '💓 Alive and kicking!', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
