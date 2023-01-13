import psycopg2
from dotenv import load_dotenv
import os

load_dotenv('.env', override=True)

print(os.getenv('PROJECT_NAME'))
host = os.getenv('HOST')
port = os.getenv('PORT')
dbname = os.getenv('DBNAME')
user = os.getenv('USER')
password = os.getenv('PASSWORD')

# Connect to your PostgreSQL database on a remote server / for now its local 127.0.0.1
conn = psycopg2.connect(host=host, port=port, dbname=dbname, user=user, password=password)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a test query
# cur.execute("INSERT INTO song_table (song, hour, minute) VALUES (%s, %s, %s);", ("hehe.mp3", 18, 22))
# conn.commit()
cur.execute("SELECT * FROM song_table;")

# Retrieve query results
records = cur.fetchall()

# Finally, you may print the output to the console or use it anyway you like
print(records)

# Close communication with the database
cur.close()
conn.close()