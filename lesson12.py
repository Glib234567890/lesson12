import sqlite3
from bs4 import BeautifulSoup
import requests

conn = sqlite3.connect("sites.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS sites (url TEXT)")

link = "https://en.wikipedia.org/wiki/Python_(programming_language)"
cursor.execute("INSERT OR IGNORE INTO sites (url) VALUES (?)", (link,))
conn.commit()

keyword = "python"
response = requests.get(link)
text = BeautifulSoup(response.text, 'html.parser').get_text().lower()
count = text.split().count(keyword)

print(f"Слово '{keyword}' зустрічається {count} разів на сторінці {link}")

conn.close()
