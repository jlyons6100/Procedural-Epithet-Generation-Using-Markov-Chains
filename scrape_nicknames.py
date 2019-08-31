from bs4 import BeautifulSoup
import requests
import sqlite3
# Scrapes nicknames from game of thrones wiki and puts them directly in database
conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS epithets
             (epithet text PRIMARY KEY)''')

page_link = 'https://gameofthronesfanon.fandom.com/wiki/Nickname'
page_response = requests.get(page_link, timeout=5)
page_content = BeautifulSoup(page_response.content, "html.parser")

i = 0
while(True):
	try:
		string = page_content.find_all("b")[i].text
		if string[0] == "\"": # Strip quotes
			sql = "INSERT OR IGNORE INTO epithets(epithet) VALUES(?)"
			c.execute(sql, (string[1:-1],))
		i += 1
	except:
		break

# c.execute("SELECT * FROM epithets")
# rows = c.fetchall()
# for row in rows:
#     print(row)
    
conn.commit()
conn.close()

