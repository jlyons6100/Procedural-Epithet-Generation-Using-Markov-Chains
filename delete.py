from collections import defaultdict, Counter
import sqlite3
from markov_chain import Markov_Chain
import random

# Deleted mistakes in database
conn = sqlite3.connect('database.db')
c = conn.cursor()

graph = {} # Word to next word/probability
c.execute("SELECT * FROM epithets")
rows = c.fetchall()
for row in rows:
    mycounter = Counter(row[0])
    if mycounter['\''] == 2:
       	string = row[0].replace("\'", "", 1)
        sql = 'DELETE FROM epithets WHERE epithet=?'
       	c.execute(sql, (row[0],))
        sql = "INSERT OR IGNORE INTO epithets(epithet) VALUES(?)"
        c.execute(sql, (string,))


conn.commit()
conn.close()
