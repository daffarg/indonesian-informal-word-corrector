import mariadb
import sys
from string_matching import kmpMatch, bmMatch

try:
    conn = mariadb.connect(
        user="root",
        password="Jakarta06",
        host="LAPTOP-5P9LFIRM",
        port=1234,
        database="kata_baku"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

dictKata = {}

# Dapatkan data pasangan kata baku dan tidak baku dari basis data
cur.execute("SELECT * FROM pasangan_kata")
for (id, tidakBaku, baku) in cur:
    dictKata[tidakBaku] = baku

conn.close()

fileName = input("Masukkan nama file: ")
try:
    with open(fileName) as f:
        lines = [line.rstrip() for line in f]
except:
    print("File tidak ditemukan")
    sys.exit(1)

print("Algoritma Pencocokan String:\n1. Knuth-Morris-Pratt (KMP)\n2. Booyer-Moore")
while True:
    try: 
        algorithm = int(input("Pilihan algoritma (1 atau 2): "))
    except:
        print('Masukkan input "1" atau "2" saja!')
        continue
    if (algorithm == 1 or algorithm == 2):
        break
    else:
        print('Masukkan input "1" atau "2" saja!')
        continue

# Lakukan pengoreksian kata tidak baku
for i in range(len(lines)):
    for key in dictKata:
        if (algorithm == 1):
            result = kmpMatch(key.casefold(), lines[i].casefold())
        else:               
            result = bmMatch(key.casefold(), lines[i].casefold())
        if (result != -1):
            oldWord = lines[i][result : result + len(key)]
            newWord = dictKata[key]
            if (oldWord[0].isupper()):
                newWord = newWord.capitalize()            
            lines[i] = lines[i].replace(oldWord, newWord)

print("\nHasil pengoreksian kata tidak baku:\n")
for j in range(len(lines)):
    print(lines[j])