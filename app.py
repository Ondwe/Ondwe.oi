from flask import Flask, request, jsonify
import openai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows frontend requests

# Set up OpenAI API Key (Replace with your own)
openai.api_key = "your_openai_api_key"

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get("prompt", "")

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    generated_text = response["choices"][0]["message"]["content"]

    return jsonify({"generatedText": generated_text})

if __name__ == '__main__':
    app.run(debug=True)