from flask import Flask, request, jsonify, render_template
import openai
import os

# Set up Flask app and OpenAI API key
app = Flask(__name__)
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Define route to render HTML template
@app.route("/")
def home():
    return render_template("index.html")

# Run app
if __name__ == "__main__":
    app.run()

# Define route for API endpoint
@app.route("/api", methods=["POST"])
def api():
    # Get question from form data
    question = request.json["question"]
    
    # Use OpenAI to generate answer
    response = openai.Completion.create(
        engine="text-davinci-002", prompt=f"Q: {question}\nA:", max_tokens=1024, n=1, stop=None, temperature=0.7,
    )
    answer = response.choices[0].text.strip()
    
    # Return answer as JSON
    return jsonify({"answer": answer})

# Run app
if __name__ == "__main__":
    app.run()
