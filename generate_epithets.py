from bs4 import BeautifulSoup
import requests
import sqlite3

nicknames = []
materials = ['Stone','Steel','Wood','Dirt','Shadow','Wind']
directions = ['West','North','South','East']
relations = ['Daughter','Son','Father','Mother']
places = ['Moon','Sun','Abyss','Nightmare','Death','Grave']
age = ['Young','Old']
animals = ['Bearshark','Lion','Tiger','Dragonfly', 'Raven', 'Eagle', 'Wolf','Bull','Toad','Snake']
monsters = ['Draugr','Dragon','Kraken','Wyrm','Minotaur','Angel','Demon','Reaper']
titles = ['Crusher','Knight','Surgeon','Swindler','Master','Tyrant','King','Warden','Bastard','Lord']
colors = ['Red','Black','White','Blue','Green']
time = ['Dusk', 'Night','Evening','Morning']
environments = ['Sky', 'River','Ocean','Tundra']
sizes = ['Grand','Proud','Molten','Wild','Light','Dark']
bodyparts = ['Finger','Fist','Toe','Hand','Mind','Claw','Tooth','Blood','Branch','Heart']

# Created random generated names inspired by GOT epithets and added them to the data base
def insert(string):
	print('The '+string)
	while(True):
		choice = input('1 skip, 2 insert')
		if choice == '1':
			return
		elif choice == '2':
			break
	sql = "INSERT OR IGNORE INTO epithets(epithet) VALUES(?)"
	c.execute(sql, ('The '+string,))

def fill_nicknames(n):
	for col in colors:
		for a in animals:
			string = col + " " + a
			insert(string)
		for a in monsters:
			string = col + " " + a
			insert(string)
		for a in titles:
			string = col + " " + a
			insert(string)
		for a in time:
			string = col + " " + a
			insert(string)
	for col in materials:
		for a in animals:
			string = col + " " + a
			insert(string)
		for a in monsters:
			string = col + " " + a
			insert(string)
		for a in titles:
			string = col + " " + a
			insert(string)
		for a in time:
			string = col + " " + a
			insert(string)
	for col in materials + places:
		for a in animals:
			string = col + " " + a
			insert(string)
		for a in monsters:
			string = col + " " + a
			insert(string)
		for a in titles:
			string = col + " " + a
			insert(string)
		for a in time:
			string = col + " " + a
			insert(string)
	for col in  directions:
		for a in monsters:
			string = a + " of the " + col
			insert(string)
		for a in animals:
			string = a + " of the " + col
			insert(string)
	for col in titles:
		for a in animals:
			string = col + " of the " + a + "s"
			insert(string)
		for a in monsters:
			string = col + " of the " + a + "s"
			insert(string)
		for a in time:
			string = col + " of the " + a + "s"
			insert(string)
	for col in monsters + animals + environments + places:
		for a in bodyparts + relations:
			string = col + "'s' " + a
			insert(string)
	for col in age + sizes:
		for a in animals + monsters:
			string = col + " " + a
			insert(string)
conn = sqlite3.connect('database.db',timeout=10)
c = conn.cursor()
fill_nicknames(nicknames)
conn.commit()
conn.close()

