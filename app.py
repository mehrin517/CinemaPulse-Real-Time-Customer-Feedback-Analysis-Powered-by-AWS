from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.secret_key = "cinemapulse_secret_key"


# -------- CACHED PAGE PREVENTION --------
@app.after_request
def prevent_cache(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response


# -------- MYSQL CONFIG --------
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'movie_feedback',
    'port': 3306
}

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)


# -------- HOME --------
@app.route('/')
def index():
    return render_template('index.html')


# -------- ABOUT --------
@app.route('/about')
def about():
    return render_template('about.html')


# -------- CONTACT --------
@app.route('/contact')
def contact():
    return render_template('contact.html')


# -------- LOGIN --------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True, buffered=True)

        cursor.execute(
            "SELECT * FROM users WHERE email=%s AND password=%s",
            (email, password)
        )
        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if user:
            session['user_id'] = user['user_id']
            session['username'] = user['username']
            return redirect(url_for('movie_list'))

        return render_template('login.html', error="Invalid email or password")

    return render_template('login.html')


# -------- SIGNUP --------
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        # Validate passwords match
        if password != confirm_password:
            return render_template('signup.html', error="Passwords do not match")

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True, buffered=True)

        # Check if email already exists
        cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
        existing_user = cursor.fetchone()

        if existing_user:
            cursor.close()
            conn.close()
            return render_template('signup.html', error="Email already registered")

        # Insert new user
        try:
            cursor.execute(
                "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                (username, email, password)
            )
            conn.commit()
            cursor.close()
            conn.close()
            return render_template('signup.html', success="Account created successfully! You can now sign in.")
        except Exception as e:
            cursor.close()
            conn.close()
            return render_template('signup.html', error="Error creating account. Please try again.")

    return render_template('signup.html')


# -------- MOVIE LIST --------
@app.route('/movies')
def movie_list():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM movies")
    movies = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('movie.html', movies=movies)


# -------- FEEDBACK --------
@app.route('/feedback/<int:movie_id>', methods=['GET', 'POST'])
def feedback(movie_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT movie_name FROM movies WHERE movie_id=%s",
        (movie_id,)
    )
    movie = cursor.fetchone()

    if not movie:
        cursor.close()
        conn.close()
        return "Movie not found"

    if request.method == 'POST':
        rating = request.form.get('rating')
        comment = request.form.get('comment')

        cursor.execute("""
            INSERT INTO feedback (user_id, movie_id, rating, comment)
            VALUES (%s, %s, %s, %s)
        """, (
            session['user_id'],
            movie_id,
            rating,
            comment
        ))
        conn.commit()

        cursor.close()
        conn.close()
        return redirect(url_for('thankyou'))

    # Fetch all feedback for this movie with usernames
    cursor.execute("""
        SELECT f.rating, f.comment, u.username, f.feedback_date
        FROM feedback f
        JOIN users u ON f.user_id = u.user_id
        WHERE f.movie_id = %s
        ORDER BY f.feedback_date DESC
    """, (movie_id,))
    
    all_feedback = cursor.fetchall()
    feedback_count = len(all_feedback)

    cursor.close()
    conn.close()

    return render_template(
        'feedback.html',
        movie_title=movie['movie_name'],
        movie_id=movie_id,
        feedback=all_feedback,
        feedback_count=feedback_count
    )


# -------- THANK YOU --------
@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


# -------- LOGOUT --------
@app.route('/logout')
def logout():
    session.clear()
    response = redirect(url_for('index'))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response


# -------- RUN --------
if __name__ == '__main__':
    app.run(debug=True)
