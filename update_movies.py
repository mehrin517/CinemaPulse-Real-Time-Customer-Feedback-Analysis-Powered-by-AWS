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

# Latest Bollywood Movies (2021-2026) with working poster placeholder images and YouTube search links
movies = [
    ("Chhaava", 2026, "https://via.placeholder.com/300x450/1a1a1a/ff1744?text=Chhaava", "https://www.youtube.com/results?search_query=Chhaava+trailer"),
    ("Fighter", 2024, "https://via.placeholder.com/300x450/1a1a1a/ff1744?text=Fighter", "https://www.youtube.com/results?search_query=Fighter+2024+trailer"),
    ("Bade Miyan Chote Miyan", 2024, "https://via.placeholder.com/300x450/1a1a1a/ff1744?text=BMCM", "https://www.youtube.com/results?search_query=Bade+Miyan+Chote+Miyan+trailer"),
    ("Article 370", 2024, "https://via.placeholder.com/300x450/1a1a1a/ff1744?text=Article+370", "https://www.youtube.com/results?search_query=Article+370+trailer"),
    ("Maharaja", 2024, "https://via.placeholder.com/300x450/1a1a1a/ff1744?text=Maharaja", "https://www.youtube.com/results?search_query=Maharaja+trailer"),
    ("Singham Again", 2024, "https://via.placeholder.com/300x450/1a1a1a/ff1744?text=Singham+Again", "https://www.youtube.com/results?search_query=Singham+Again+trailer"),
    ("Bhool Bhulaiyaa 3", 2024, "https://via.placeholder.com/300x450/1a1a1a/ff1744?text=Bhool+Bhulaiyaa+3", "https://www.youtube.com/results?search_query=Bhool+Bhulaiyaa+3+trailer"),
    ("Khel Khel Mein", 2024, "https://via.placeholder.com/300x450/1a1a1a/ff1744?text=Khel+Khel+Mein", "https://www.youtube.com/results?search_query=Khel+Khel+Mein+trailer"),
    ("Pathaan", 2023, "https://via.placeholder.com/300x450/1a1a1a/ff1744?text=Pathaan", "https://www.youtube.com/results?search_query=Pathaan+trailer"),
    ("Gadar 2", 2023, "https://via.placeholder.com/300x450/1a1a1a/ff1744?text=Gadar+2", "https://www.youtube.com/results?search_query=Gadar+2+trailer"),
    ("Jawan", 2023, "https://via.placeholder.com/300x450/1a1a1a/ff1744?text=Jawan", "https://www.youtube.com/results?search_query=Jawan+trailer"),
    ("Munjya", 2023, "https://via.placeholder.com/300x450/1a1a1a/ff1744?text=Munjya", "https://www.youtube.com/results?search_query=Munjya+trailer"),
    ("12th Fail", 2023, "https://via.placeholder.com/300x450/1a1a1a/ff1744?text=12th+Fail", "https://www.youtube.com/results?search_query=12th+Fail+trailer"),
    ("Drishyam 2", 2023, "https://via.placeholder.com/300x450/1a1a1a/ff1744?text=Drishyam+2", "https://www.youtube.com/results?search_query=Drishyam+2+trailer"),
    ("Bhool Bhulaiyaa 2", 2022, "https://via.placeholder.com/300x450/1a1a1a/ff1744?text=BB2", "https://www.youtube.com/results?search_query=Bhool+Bhulaiyaa+2+trailer"),
    ("Brahmastra", 2022, "https://via.placeholder.com/300x450/1a1a1a/ff1744?text=Brahmastra", "https://www.youtube.com/results?search_query=Brahmastra+trailer"),
    ("Runway 34", 2022, "https://via.placeholder.com/300x450/1a1a1a/ff1744?text=Runway+34", "https://www.youtube.com/results?search_query=Runway+34+trailer"),
    ("Khuda Haafiz Chapter 2", 2022, "https://via.placeholder.com/300x450/1a1a1a/ff1744?text=Khuda+Haafiz", "https://www.youtube.com/results?search_query=Khuda+Haafiz+Chapter+2+trailer"),
    ("An Action Hero", 2022, "https://via.placeholder.com/300x450/1a1a1a/ff1744?text=Action+Hero", "https://www.youtube.com/results?search_query=An+Action+Hero+trailer"),
    ("Badhaai Ho", 2022, "https://via.placeholder.com/300x450/1a1a1a/ff1744?text=Badhaai+Ho", "https://www.youtube.com/results?search_query=Badhaai+Ho+trailer"),
    ("Sooryavanshi", 2021, "https://via.placeholder.com/300x450/1a1a1a/ff1744?text=Sooryavanshi", "https://www.youtube.com/results?search_query=Sooryavanshi+trailer"),
    ("Shershaah", 2021, "https://via.placeholder.com/300x450/1a1a1a/ff1744?text=Shershaah", "https://www.youtube.com/results?search_query=Shershaah+trailer"),
]

try:
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Delete existing movies
    cursor.execute("DELETE FROM movies")
    conn.commit()
    print("Cleared existing movies")
    
    # Insert new movies
    insert_query = "INSERT INTO movies (movie_name, release_year, poster_url, trailer_url) VALUES (%s, %s, %s, %s)"
    cursor.executemany(insert_query, movies)
    conn.commit()
    
    print(f"Successfully added {cursor.rowcount} movies with working URLs!")
    
    cursor.close()
    conn.close()
    
except Exception as e:
    print(f"Error: {e}")
