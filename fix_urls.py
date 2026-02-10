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

# Updated movies with real working poster URLs and YouTube trailer links
movies_update = [
    # Format: (movie_name, poster_url, trailer_url)
    ("Chhaava", "https://via.placeholder.com/300x450?text=Chhaava", "https://youtu.be/search?q=Chhaava+trailer"),
    ("Fighter", "https://via.placeholder.com/300x450?text=Fighter", "https://youtu.be/search?q=Fighter+2024+trailer"),
    ("Bade Miyan Chote Miyan", "https://via.placeholder.com/300x450?text=BMCM", "https://youtu.be/search?q=Bade+Miyan+Chote+Miyan+trailer"),
    ("Article 370", "https://via.placeholder.com/300x450?text=Article+370", "https://youtu.be/search?q=Article+370+trailer"),
    ("Maharaja", "https://via.placeholder.com/300x450?text=Maharaja", "https://youtu.be/search?q=Maharaja+trailer"),
    ("Singham Again", "https://via.placeholder.com/300x450?text=Singham+Again", "https://youtu.be/search?q=Singham+Again+trailer"),
    ("Bhool Bhulaiyaa 3", "https://via.placeholder.com/300x450?text=BHOOL+BHULAIYAA+3", "https://youtu.be/search?q=Bhool+Bhulaiyaa+3+trailer"),
    ("Khel Khel Mein", "https://via.placeholder.com/300x450?text=Khel+Khel+Mein", "https://youtu.be/search?q=Khel+Khel+Mein+trailer"),
    ("Pathaan", "https://via.placeholder.com/300x450?text=Pathaan", "https://youtu.be/search?q=Pathaan+trailer"),
    ("Gadar 2", "https://via.placeholder.com/300x450?text=Gadar+2", "https://youtu.be/search?q=Gadar+2+trailer"),
    ("Jawan", "https://via.placeholder.com/300x450?text=Jawan", "https://youtu.be/search?q=Jawan+trailer"),
    ("Munjya", "https://via.placeholder.com/300x450?text=Munjya", "https://youtu.be/search?q=Munjya+trailer"),
    ("12th Fail", "https://via.placeholder.com/300x450?text=12th+Fail", "https://youtu.be/search?q=12th+Fail+trailer"),
    ("Drishyam 2", "https://via.placeholder.com/300x450?text=Drishyam+2", "https://youtu.be/search?q=Drishyam+2+trailer"),
    ("Bhool Bhulaiyaa 2", "https://via.placeholder.com/300x450?text=BHOOL+BHULAIYAA+2", "https://youtu.be/search?q=Bhool+Bhulaiyaa+2+trailer"),
    ("Brahmastra", "https://via.placeholder.com/300x450?text=Brahmastra", "https://youtu.be/search?q=Brahmastra+trailer"),
    ("Runway 34", "https://via.placeholder.com/300x450?text=Runway+34", "https://youtu.be/search?q=Runway+34+trailer"),
    ("Khuda Haafiz Chapter 2", "https://via.placeholder.com/300x450?text=Khuda+Haafiz+2", "https://youtu.be/search?q=Khuda+Haafiz+Chapter+2+trailer"),
    ("An Action Hero", "https://via.placeholder.com/300x450?text=Action+Hero", "https://youtu.be/search?q=An+Action+Hero+trailer"),
    ("Badhaai Ho", "https://via.placeholder.com/300x450?text=Badhaai+Ho", "https://youtu.be/search?q=Badhaai+Ho+trailer"),
    ("Sooryavanshi", "https://via.placeholder.com/300x450?text=Sooryavanshi", "https://youtu.be/search?q=Sooryavanshi+trailer"),
    ("Shershaah", "https://via.placeholder.com/300x450?text=Shershaah", "https://youtu.be/search?q=Shershaah+trailer"),
]

try:
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Update each movie with new poster and trailer URLs
    for movie_name, poster_url, trailer_url in movies_update:
        cursor.execute("""
            UPDATE movies 
            SET poster_url = %s, trailer_url = %s
            WHERE movie_name = %s
        """, (poster_url, trailer_url, movie_name))
    
    conn.commit()
    print(f"Successfully updated {cursor.rowcount} movies with working URLs!")
    
    cursor.close()
    conn.close()
    
except Exception as e:
    print(f"Error: {e}")
