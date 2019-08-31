import random

class Markov_Chain:
	def __init__(self, table, start_state):
		self.table = table
		self.state = start_state
	def step(self):
		r = random.random()
		s = 0
		if self.state not in self.table: # Absorbing State - Impossible to leave
			return ""
		for word2 in self.table[self.state]:
			s += self.table[self.state][word2]
			if r <= s:
				self.state = word2
				return word2
		return ""