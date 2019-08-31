from collections import defaultdict
import sqlite3
from markov_chain import Markov_Chain
import random

conn = sqlite3.connect('database.db')
c = conn.cursor()


graph = {} # Word to next word/probability
c.execute("SELECT * FROM epithets")
rows = c.fetchall()
def get_counts():    
    for row in rows:
        epithet = row[0].split(" ")
        for i in range(len(epithet) - 1):
            word1 = epithet[i]
            word1.lower()
            word2 = epithet[i + 1]
            word2.lower()
            if not word1 in graph:
                graph[word1] = {}
            if word2 in graph[word1]:
                graph[word1][word2] += 1
            else:
                graph[word1][word2] = 1
def get_probabilities():
    for word1 in graph:
    	summ = 0
    	for word2 in graph[word1]:
    		summ += graph[word1][word2]
    	for word2 in graph[word1]:
    		graph[word1][word2] = graph[word1][word2] / summ
get_counts()
get_probabilities()

generated = 'The'
r = random.random()
if r >= 0.5:
    generated = random.choice(list(graph))
m_chain = Markov_Chain(graph, generated)
for i in range(30):
    for x in range(30):
        nextt = m_chain.step()
        if nextt == "": # Absorbing state
            print(generated)
            generated = 'The'
            r = random.random()
            if r >= 0.5:
                generated = random.choice(list(graph))
            m_chain.state = generated
            break
        generated += " "+nextt
        


# conn.commit()
conn.close()
