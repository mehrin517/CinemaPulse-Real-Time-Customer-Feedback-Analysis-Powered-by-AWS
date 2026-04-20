# Cinema Pulse

A Flask-based movie rating website built with HTML, CSS, and Python.

**CinemaPulse: Real-Time Customer Feedback Analysis Powered by AWS**

CinemaPulse is a Flask-based movie feedback application that captures customer ratings and comments and performs real-time sentiment analysis using AWS services. The app provides two deployment modes:

**Mode 1: Local MySQL + AWS Sentiment Analysis (app.py)**
- Uses local MySQL database for user and feedback storage
- Optional AWS Comprehend integration for real-time sentiment analysis
- Sentiment results stored in dedicated `feedback_sentiment` table
- Built-in fallback when AWS services are unavailable

**Mode 2: Full AWS Backend (aws_app.py)**
- Uses AWS DynamoDB for scalable user and feedback storage
- AWS SNS for notifications (password reset, new user alerts)
- Advanced analytics with vibe-based feedback (Mind-Blowing, Heartwarming, Tear-Jerker, Edge-of-Seat, Pure-Joy, Thought-Provoking)
- Radar chart comparison for multi-movie analysis
- Production-ready with secure token-based password reset

## Setup

### Prerequisites
- Python 3.8+
- MySQL

### Installation

1. Clone and install dependencies:
```bash
pip install -r requirements.txt
```

```
3. Run the app:

python app.py
```

4. Open your browser at `http://127.0.0.1:5000`

## Features

- **User Authentication**: Secure login/signup with password hashing
- **Feedback Submission**: Rate and comment on movies with emotion classification
- **Analytics Dashboard**: View feedback trends, top-rated movies, and vibe distributions

## Project Structure

- `app.py` - Local MySQL mode with optional Comprehend
- `aws_app.py`
- `templates/` 
- `static/` - CSS and frontend assets
- `requirements.txt` - Python dependencies

