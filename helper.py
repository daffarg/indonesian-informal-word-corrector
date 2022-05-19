# Module Imports
import mariadb
import sys
from daftar_kata import daftar

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="your_password",
        host="your_host",
        port=1234,
        database="kata_baku"
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