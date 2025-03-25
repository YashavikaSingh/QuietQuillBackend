from flask import Flask, request, jsonify
from textblob import TextBlob
from flask_cors import CORS
import google.generativeai as genai
import os

app = Flask(__name__)
CORS(app)

# Configure the Gemini API key
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("The GOOGLE_API_KEY environment variable is not set.")
genai.configure(api_key=GOOGLE_API_KEY)

# Load the Gemini model outside of routes
gemini_model = genai.GenerativeModel('gemini-pro')

@app.route('/analyze_sentiment/', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    note = data.get("note", "")

    # Perform sentiment analysis using TextBlob
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
    data = request.get_json()
    diary_entry = data.get('text', '')

    # Craft a prompt for Gemini to act as a therapist
    prompt = f"""
    You are a compassionate and understanding therapist. A client has shared the following diary entry:

    "{diary_entry}"

    Respond to this diary entry as a therapist would. Offer insights, support, and perhaps some gentle guidance or questions to help them reflect further. Keep your response empathetic and encouraging.
    """

    # Generate text using Gemini with the crafted prompt
    try:
        response = gemini_model.generate_content(prompt)
        therapist_response = response.text
    except Exception as e:
        return jsonify({"error": f"Error during text generation: {str(e)}"}), 500

    return jsonify({'suggestion': therapist_response})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)
