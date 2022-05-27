# Insert daftar kata baku ke dalam database MariaDB

# Module Imports
import mariadb
import sys
from daftar_kata import daftar

# Connect to MariaDB Platform
try: # change the arguments
    conn = mariadb.connect(
        user="your_user", # your user
        password="your_password", # your password
        host="your_host", # your host
        port=1234, # your port
        database="your_database" # your database
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

cur.execute("DELETE FROM pasangan_kata")
for tidak_baku, baku in daftar.items():
    cur.execute("INSERT INTO pasangan_kata(tidak_baku, baku) VALUES(?,?)", (tidak_baku, baku,))

conn.commit()
conn.close()