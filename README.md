# Cinema Pulse

A Flask-based movie rating website built with HTML, CSS, and Python.

## Features

- Browse a collection of movies
- User authentication
- Rate movies with mood, score, and comments
- Responsive design with Tailwind CSS

## Run Locally

**Prerequisites:** Python 3.8+

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the app:
   ```bash
   python app.py
   ```

3. Open your browser to `http://127.0.0.1:5000`

## Database Setup

The app is configured to use AWS RDS MySQL. Update the `DB_CONFIG` in `app.py` with your database credentials.

For local development, ratings are currently printed to console. Update the code to save to your database.
