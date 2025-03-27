from flask import Flask, request, jsonify
from textblob import TextBlob
from flask_cors import CORS
import google.generativeai as genai
import os
import datetime

app = Flask(__name__)
CORS(app)

# Configure the Gemini API key
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("The GOOGLE_API_KEY environment variable is not set.")
genai.configure(api_key=GOOGLE_API_KEY)

# Use the correct Gemini model initialization
try:
    gemini_model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    print(f"Failed to load Gemini model: {str(e)}")
    exit(1)

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

    # Properly format the input prompt for Gemini
    prompt = f"""
    You are a compassionate and understanding therapist. A client has shared the following diary entry:

    "{diary_entry}"

    Respond to this diary entry as a therapist would. Offer insights, support, and perhaps some gentle guidance or questions to help them reflect further. Keep your response empathetic and encouraging.
    """

    # Use the generate_content method correctly
    try:
        response = gemini_model.generate_content(prompt)
        therapist_response = response.text
    except Exception as e:
        return jsonify({"error": f"Error during text generation: {str(e)}"}), 500

    return jsonify({'suggestion': therapist_response})

@app.route('/monthly_summary', methods=['POST'])
def generate_monthly_summary():
    data = request.get_json()
    month = data.get('month', '')
    diary_entries = data.get('entries', [])

    # Combine all entries into a single context
    combined_entries = "\n\n".join(diary_entries)

    # Prompt for generating a comprehensive monthly summary
    prompt = f"""
    You are an insightful life coach analyzing a person's diary entries for {month}. 
    Provide a structured summary covering:

    - **Relationships (Friends, Partner, Family)**:
    - Social interactions and dynamics  
    - Significant moments or challenges  

    - **Work/Study Progress**:
    - Key achievements, challenges, or learnings  

    - **Exercise and Well-being**:
    - Fitness activities and self-care patterns  

    - **Emotional Landscape**:
    - Recurring emotional themes  
    - Sources of stress, anxiety, or joy  
    - Areas for emotional growth  

    - **Writing and Self-Expression**:
    - Evolution of writing style  
    - Improvements in articulation and reflection  

    - **Notable Milestones and Experiences**:
    - Chronological list of key events  
    - Personal growth highlights  

    **Diary Entries Context:**  
    {combined_entries}  

    Please provide a clear, empathetic, and constructive analysis.
    """

    # Generate summary using Gemini
    try:
        response = gemini_model.generate_content(prompt)
        monthly_summary = response.text
    except Exception as e:
        return jsonify({"error": f"Error during monthly summary generation: {str(e)}"}), 500

    return jsonify({'summary': monthly_summary})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)