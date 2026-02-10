import mysql.connector

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'movie_feedback',
    'port': 3306
}

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

# Latest Bollywood Movies (2021-2026) with posters and trailers
movies = [
    # 2026
    ("Chhaava", 2026, "https://m.media-amazon.com/images/M/MV5BZjk4ODMzMTktOWIyMi00YzA2LWE2NTEtNTc5MGE0NjI0NTQyXkEyXkFqcGdeQXVyMTIyNzAyNDA1._V1_SX300.jpg", "https://www.youtube.com/embed/trailer1"),
    
    # 2024
    ("Fighter", 2024, "https://m.media-amazon.com/images/M/MV5BZGZmNzFlNTAtMDNkYi00MjU3LWFlMDItMTUwMjU4OGFkOTczXkEyXkFqcGdeQXVyMTUzNTg3NjQx._V1_SX300.jpg", "https://www.youtube.com/embed/Fighter_trailer"),
    ("Bade Miyan Chote Miyan", 2024, "https://m.media-amazon.com/images/M/MV5BOGQzNTliODAtMzQ3ZC00OWZjLWE1ZDItYjNhYzQ5OGQ4ZDZiXkEyXkFqcGdeQXVyMTQ3Mzc4NjI0._V1_SX300.jpg", "https://www.youtube.com/embed/BMCM_trailer"),
    ("Article 370", 2024, "https://m.media-amazon.com/images/M/MV5BMjYzOTJiMTItZDQxMC00YTE0LTk4MjAtN2M5MTJhMzQ0YTAyXkEyXkFqcGdeQXVyMTUzNTg3NjQx._V1_SX300.jpg", "https://www.youtube.com/embed/Article370_trailer"),
    ("Maharaja", 2024, "https://m.media-amazon.com/images/M/MV5BYjQ3OWExMTctYzBhYi00NTY2LWE2YjAtNWM5NjI5ZjE5YzY1XkEyXkFqcGdeQXVyMDU5MTU5MjI1._V1_SX300.jpg", "https://www.youtube.com/embed/Maharaja_trailer"),
    ("Singham Again", 2024, "https://m.media-amazon.com/images/M/MV5BZWIzN2YwNTUtMjY4ZC00MjM0LWI2YTItYzc0OTJjZDc3MmQ4XkEyXkFqcGdeQXVyMTUzNTg3NjQx._V1_SX300.jpg", "https://www.youtube.com/embed/SinghamAgain_trailer"),
    ("Bhool Bhulaiyaa 3", 2024, "https://m.media-amazon.com/images/M/MV5BMmI5MDhhNDUtNjA2OC00YjdjLWJmMjktYTEzOTQ3YzI2YmY3XkEyXkFqcGdeQXVyMzY0MTE0NzA@._V1_SX300.jpg", "https://www.youtube.com/embed/BB3_trailer"),
    ("Khel Khel Mein", 2024, "https://m.media-amazon.com/images/M/MV5BY2IyODgzN2ItNTkwYi00Njg4LWI3MjItMjBmNjY5YTY4NTJiXkEyXkFqcGdeQXVyMTUzNTg3NjQx._V1_SX300.jpg", "https://www.youtube.com/embed/KhelKhel_trailer"),
    
    # 2023
    ("Pathaan", 2023, "https://m.media-amazon.com/images/M/MV5BNGFhNjBlYTItMzI3NS00NTU0LWJkNTItZTcxNDEyMTMyMzYzXkEyXkFqcGdeQXVyMTQ3Mzc4NjI0._V1_SX300.jpg", "https://www.youtube.com/embed/Pathaan_trailer"),
    ("Gadar 2", 2023, "https://m.media-amazon.com/images/M/MV5BZDg5YjA2ZmEtYmJjNi00OWJjLTk2MzAtOTc5ZmZiNTI3OGEyXkEyXkFqcGdeQXVyMTQ3Mzc4NjI0._V1_SX300.jpg", "https://www.youtube.com/embed/Gadar2_trailer"),
    ("Jawan", 2023, "https://m.media-amazon.com/images/M/MV5BZDZmNWQ3N2UtZmY3Ni00YzI1LTkwOTItOGYyYTQzNjQ3OWI3XkEyXkFqcGdeQXVyMTQ3Mzc4NjI0._V1_SX300.jpg", "https://www.youtube.com/embed/Jawan_trailer"),
    ("Munjya", 2023, "https://m.media-amazon.com/images/M/MV5BYWI3NDgyMjYtYzk1ZC00ZjM4LWFjYmItMTU1ZGM1NDUyOGQ4XkEyXkFqcGdeQXVyMTQ3Mzc4NjI0._V1_SX300.jpg", "https://www.youtube.com/embed/Munjya_trailer"),
    ("12th Fail", 2023, "https://m.media-amazon.com/images/M/MV5BOTE5ZjZhNDktMTg2Ni00YzUwLWI5NTEtNDc0ZTIwODM3MmE2XkEyXkFqcGdeQXVyMTQ3Mzc4NjI0._V1_SX300.jpg", "https://www.youtube.com/embed/12thFail_trailer"),
    ("Drishyam 2", 2023, "https://m.media-amazon.com/images/M/MV5BYmE5MjFmOWYtMjQzNC00NTI4LWJlZWQtNTlhYzI2ZjE0NWQ0XkEyXkFqcGdeQXVyMTQ3Mzc4NjI0._V1_SX300.jpg", "https://www.youtube.com/embed/Drishyam2_trailer"),
    
    # 2022
    ("Bhool Bhulaiyaa 2", 2022, "https://m.media-amazon.com/images/M/MV5BZDljMmM3NDMtMjEwZi00NjNiLWE2OTItNWYwZmRlZjg0YThkXkEyXkFqcGdeQXVyMTQ3Mzc4NjI0._V1_SX300.jpg", "https://www.youtube.com/embed/BB2_trailer"),
    ("Brahmastra", 2022, "https://m.media-amazon.com/images/M/MV5BMzA0YWU3ZTItYzI1OC00YzE4LWI4ZWUtYTdkZjZkZjI2OTQyXkEyXkFqcGdeQXVyODE4NzMyNw@@._V1_SX300.jpg", "https://www.youtube.com/embed/Brahmastra_trailer"),
    ("Runway 34", 2022, "https://m.media-amazon.com/images/M/MV5BZTE1MWIyZDItNDdmOS00ZDMxLTg0MzAtYThhYjQ1MDMyMWJmXkEyXkFqcGdeQXVyMTQ3Mzc4NjI0._V1_SX300.jpg", "https://www.youtube.com/embed/Runway34_trailer"),
    ("Khuda Haafiz Chapter 2", 2022, "https://m.media-amazon.com/images/M/MV5BZGJhNWM1NGUtZDhiYi00MzMzLTk1N2ItYjlhZDU5MWVhOWI5XkEyXkFqcGdeQXVyMTQ3Mzc4NjI0._V1_SX300.jpg", "https://www.youtube.com/embed/KhudaHaafiz2_trailer"),
    ("An Action Hero", 2022, "https://m.media-amazon.com/images/M/MV5BNDcwZDQ2OTQtMzE4My00YjQ4LTk3YTAtNTIxMDkwZWY1ZTVjXkEyXkFqcGdeQXVyMTQ3Mzc4NjI0._V1_SX300.jpg", "https://www.youtube.com/embed/ActionHero_trailer"),
    ("Badhaai Ho", 2022, "https://m.media-amazon.com/images/M/MV5BMjQwMzA1MWYtZWIxMS00N2EyLWI4MWUtYzM3ODhkMjE2YzhlXkEyXkFqcGdeQXVyMTQ3Mzc4NjI0._V1_SX300.jpg", "https://www.youtube.com/embed/BadhaiHo2_trailer"),
    
    # 2021
    ("Sooryavanshi", 2021, "https://m.media-amazon.com/images/M/MV5BOTJlNWM3ZDgtZWY5ZS00MTI1LWE4MzItMjIyZTA0YzBlN2U3XkEyXkFqcGdeQXVyMTQ3Mzc4NjI0._V1_SX300.jpg", "https://www.youtube.com/embed/Sooryavanshi_trailer"),
    ("Shershaah", 2021, "https://m.media-amazon.com/images/M/MV5BZGVkMWI0N2QtYmRkYi00YWE1LWJhZjUtZjBjZGU3NGY3ZjJlXkEyXkFqcGdeQXVyMTQ3Mzc4NjI0._V1_SX300.jpg", "https://www.youtube.com/embed/Shershaah_trailer"),
]

try:
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # First, delete existing movies (optional - comment out if you want to keep Inception)
    cursor.execute("DELETE FROM movies")
    conn.commit()
    print("Cleared existing movies")
    
    # Insert new movies
    insert_query = "INSERT INTO movies (movie_name, release_year, poster_url, trailer_url) VALUES (%s, %s, %s, %s)"
    cursor.executemany(insert_query, movies)
    conn.commit()
    
    print(f"Successfully added {cursor.rowcount} movies to the database!")
    
    cursor.close()
    conn.close()
    
except Exception as e:
    print(f"Error: {e}")
