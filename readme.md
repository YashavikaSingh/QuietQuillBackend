# QuietQuillBackend: A Journaling and Reflection API

QuietQuillBackend is a Flask-based API designed to enhance the journaling experience by providing sentiment analysis, AI-powered therapist-like suggestions, and monthly summaries of diary entries. It leverages the power of TextBlob for sentiment analysis and Google's Gemini API for generating insightful responses and summaries.

## Features

-   **Sentiment Analysis:** Analyzes the sentiment of a diary entry (positive, negative, or neutral) using TextBlob.
-   **AI-Powered Suggestions:** Generates empathetic and supportive responses to diary entries, simulating a therapist's guidance, using the Gemini API.
-   **Monthly Summary Generation:** Creates a comprehensive monthly summary of diary entries, covering relationships, work/study progress, well-being, emotional landscape, writing style, and notable milestones, using the Gemini API.

## Technologies Used

-   **Flask:** A lightweight WSGI web application framework for Python.
-   **TextBlob:** A Python library for processing textual data, used for sentiment analysis.
-   **Google Gemini API:** A powerful language model used for generating text-based responses and summaries.
-   **Flask-CORS:** A Flask extension for handling Cross-Origin Resource Sharing (CORS).
-   **Python:** The primary programming language.

## Prerequisites

-   **Python 3.x:** Ensure you have Python 3 installed on your system.
-   **Pip:** Python's package installer.
-   **Google Gemini API Key:** You'll need a valid API key from Google to use the Gemini API.
-   **Virtual Environment (Recommended):** It's highly recommended to use a virtual environment to manage project dependencies.

## Setup and Installation

1.  **Clone the Repository (if applicable):**
    ```bash
    git clone <your-repository-url>
    cd QuietQuillBackend
    ```

2.  **Create a Virtual Environment:**
    ```bash
    python3 -m venv venv
    ```

3.  **Activate the Virtual Environment:**
    -   **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```
    -   **On Windows:**
        ```bash
        venv\Scripts\activate
        ```

4.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    (If you don't have a requirements.txt file, create one with the following content and then run the above command)
    ```
    Flask
    textblob
    flask-cors
    google-generativeai
    ```

5.  **Set the Google API Key:**
    -   Set the `GOOGLE_API_KEY` environment variable with your actual API key.
    -   **On macOS/Linux:**
        ```bash
        export GOOGLE_API_KEY="your_actual_api_key"
        ```
    -   **On Windows:**
        ```bash
        set GOOGLE_API_KEY="your_actual_api_key"
        ```

6.  **Run the Application:**
    ```bash
    python app.py
    ```

    The application will start running on `http://0.0.0.0:5001/`.

## API Endpoints

### 1. `/analyze_sentiment/` (POST)

-   **Description:** Analyzes the sentiment of a given diary entry.
-   **Request Body (JSON):**
    ```json
    {
        "note": "Your diary entry text here."
    }
    ```
-   **Response (JSON):**
    ```json
    {
        "mood": "Positive" | "Negative" | "Neutral",
        "sentiment_score": -1.0 to 1.0
    }
    ```

### 2. `/generate` (POST)

-   **Description:** Generates a therapist-like response to a diary entry.
-   **Request Body (JSON):**
    ```json
    {
        "text": "Your diary entry text here."
    }
    ```
-   **Response (JSON):**
    ```json
    {
        "suggestion": "The AI-generated therapist response."
    }
    ```

### 3. `/monthly_summary` (POST)

-   **Description:** Generates a comprehensive monthly summary of diary entries.
-   **Request Body (JSON):**
    ```json
    {
        "month": "Month Name (e.g., January)",
        "entries": [
            "Diary entry 1 for the month.",
            "Diary entry 2 for the month.",
            "..."
        ]
    }
    ```
-   **Response (JSON):**
    ```json
    {
        "summary": "The AI-generated monthly summary."
    }
    ```

## Error Handling

-   The API returns a JSON response with an `error` key and a corresponding error message if any issues occur during text generation or monthly summary creation.
-   HTTP status codes are used to indicate the nature of the error (e.g., 500 for server errors).

## Contributing

If you'd like to contribute to the project, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them.
4.  Push your changes to your fork.
5.  Submit a pull request.

## License

[Specify the license for your project here, e.g., MIT License]

## Contact

Yashavika Singh - ys6668@nyu.edu
