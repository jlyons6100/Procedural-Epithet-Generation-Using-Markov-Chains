import random
from bisect import bisect
from collections import defaultdict
class M_Chain:
    def __init__(self, table):
        self.table = table
        self.prefix_sums = defaultdict(list) # Prefix sum
        self.p_no_name = defaultdict(list)
        for word1 in self.table:
            summ = 0
            for word2 in self.table[word1]:
                summ += self.table[word1][word2]
                self.prefix_sums[word1].append(summ)
                self.p_no_name[word1].append(word2)

        # print(self.prefix_sums['grand'])
        # print(self.table['grand'])
    def generate_epithet(self, chain_length):
        r = random.random()
        epithet = ['the'] if r < 0.5 else [random.choice(list(self.table))]
        for i in range(chain_length-1):
            if len(self.prefix_sums[epithet[-1]]) == 0:
                break
            last = len(self.prefix_sums[epithet[-1]]) - 1
            tot = self.prefix_sums[epithet[-1]][last]
            val = random.randint(0, tot - 1)
            ind = bisect(self.prefix_sums[epithet[-1]], val)
            epithet.append(self.p_no_name[epithet[-1]][ind])
        return ' '.join(epithet).title()
        # if nextt == "": # Absorbing state
        #     # print((' '.join(generated)).title())
        #     generated.clear()
        #     generated.append('the')
        #     r = random.random()
        #     if r >= 0.5:
        #         generated[0] = random.choice(list(graph))
        #     m_chain.state = generated[0]
        #     break
        # # generated += " "+nextt
        # generated.append(nextt)

    def step(self):
        pass
        # r = random.random()
        # s = 0
        # if self.state not in self.table: # Absorbing State - Impossible to leave
        # 	return ""
        # for word2 in self.table[self.state]:
        # 	s += self.table[self.state][word2]
        # 	if r <= s:
        # 		self.state = word2
        # 		return word2
        # return ""