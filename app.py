from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

# Add this code here to provide a root route for your website
@app.route("/")
def index():
    return "Hello from your AI Generator!"

# Initialize the OpenAI client
# Replace "YOUR_OPENAI_API_KEY" with your actual API key from Render's environment variables
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Define the API endpoint for text generation
@app.route("/generate", methods=["POST"])
def generate_text():
    # Retrieve the prompt from the incoming JSON request
    data = request.get_json()
    prompt_text = data.get("prompt")
    
    if not prompt_text:
        return jsonify({"error": "Prompt not provided"}), 400

    try:
        # Make the API call to OpenAI
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt_text}]
        )
        
        # Extract the generated text
        generated_text = completion.choices[0].message.content
        
        # Return the generated text as a JSON response
        return jsonify({"generated_text": generated_text})
        
    except Exception as e:
        # Handle any API errors
        return jsonify({"error": str(e)}), 500

# This is not needed for Gunicorn, but it's good practice for local testing
if __name__ == "__main__":
    app.run(debug=True)

