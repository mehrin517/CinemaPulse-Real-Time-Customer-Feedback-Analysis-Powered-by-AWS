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

try:
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Add poster_url and trailer_url columns if they don't exist
    cursor.execute("""
        ALTER TABLE movies 
        ADD COLUMN poster_url VARCHAR(500) DEFAULT NULL,
        ADD COLUMN trailer_url VARCHAR(500) DEFAULT NULL
    """)
    conn.commit()
    print("Successfully added poster_url and trailer_url columns!")
    
except Exception as e:
    if "Duplicate column" in str(e):
        print("Columns already exist")
    else:
        print(f"Error: {e}")
finally:
    cursor.close()
    conn.close()
