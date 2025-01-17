from flask import Flask, request, jsonify
from textblob import TextBlob
from flask_cors import CORS  # Add this import for CORS handling
from transformers import pipeline  # Move this import up with the others

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the model outside of routes to prevent reloading on each request
generator = pipeline('text-generation', model='gpt2')

@app.route('/analyze_sentiment/', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    note = data.get("note", "")

    # Perform sentiment analysis
    analysis = TextBlob(note)
    sentiment_score = analysis.sentiment.polarity  # Score between -1 and 1

    # Categorize sentiment
    if sentiment_score > 0.2:
        mood = "Positive"
    elif sentiment_score < -0.2:
        mood = "Negative"
    else:
        mood = "Neutral"

    return jsonify({
        "mood": mood,
        "sentiment_score": sentiment_score
    })

@app.route('/generate', methods=['POST'])
def generate_suggestion():
    # Get input text from the POST request
    data = request.get_json()
    input_text = data.get('text', '')

    # Generate text using the model
    suggestion = generator(input_text, max_length=1000)

    # Return the suggestion as JSON
    return jsonify({'suggestion': suggestion[0]['generated_text']})


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)