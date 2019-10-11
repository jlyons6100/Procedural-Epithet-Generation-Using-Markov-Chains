from collections import defaultdict
import sqlite3
from collections import defaultdict
from markov_chain import M_Chain
NUMBER_OF_EPITHETS = 30
MAX_CHAIN_LENGTH = 25
def make_table(rows):
    table = defaultdict(lambda: defaultdict(int))    
    for row in rows:
        epithet = row[0].split(" ")
        for i in range(len(epithet) - 1):
            word1 = epithet[i].lower()
            word2 = epithet[i + 1].lower()
            table[word1][word2] += 1
    return table

conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute("SELECT * FROM epithets")
rows = c.fetchall()
 # Word to next word/probability
table = make_table(rows)
m_chain = M_Chain(table)
for i in range(NUMBER_OF_EPITHETS):
    print(m_chain.generate_epithet(MAX_CHAIN_LENGTH))

# generated = ['the']
# r = random.random()
# if r >= 0.5:
#     generated[0] = random.choice(list(graph))
# m_chain = Markov_Chain(graph, generated[0])
# for i in range(30):
#     for x in range(30):
#         nextt = m_chain.step()
#         if nextt == "": # Absorbing state
#             # print((' '.join(generated)).title())
#             generated.clear()
#             generated.append('the')
#             r = random.random()
#             if r >= 0.5:
#                 generated[0] = random.choice(list(graph))
#             m_chain.state = generated[0]
#             break
#         # generated += " "+nextt
#         generated.append(nextt)
        


# conn.commit()
conn.close()
