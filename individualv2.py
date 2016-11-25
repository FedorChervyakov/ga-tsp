import math
import random


class Traveler:
	# Single individual

	# Size of genome (number of cities)
	size = 0
	# Genome is array of nodes (cities)
	# They are conected in the same order as in the array
	genome = []

	fitness = 0

	def __init__(self,nsize,gnme=[]):
		self.size = nsize
		self.genome = []
		if len(gnme) == 0:
			i = 0
			nodes = []
			while i != self.size:
				nodes.append(i)
				i += 1
			i = 0
			while i != self.size:
				node = random.choice(nodes)
				nodes.remove(node)
				self.genome.append(node)
				i += 1
		else:
			self.genome.extend(gnme)

	# Switch nodes that are next to each other
	def mutate(self,mutate_rate):
		x = random.random()
		if x < mutate_rate:
			for i in range(1,random.randint(2,int(self.size/1.5))):
				node1 = random.choice(self.genome)
				i1 = self.genome.index(node1)
				self.genome.remove(node1)
				node2 = self.genome[i1-random.choice([1,2,3])]
				i2 = self.genome.index(node2)
				self.genome.remove(node2)
				self.genome.insert(i1,node2)
				self.genome.insert(i2,node1)

	# Switch two random nodes			
	def mutatev3(self,mutate_rate):
		x = random.random()
		if x < mutate_rate:
			for i in range(0,int(self.size/4)):
				node1 = random.choice(self.genome)
				i1 = self.genome.index(node1)
				self.genome.remove(node1)
				node2 = random.choice(self.genome)
				while node2 == node1: 
					node2 = random.choice(self.genome)
				i2 = self.genome.index(node2)
				self.genome.remove(node2)
				self.genome.insert(i1,node2)
				self.genome.insert(i2,node1)

	# Switch few nodes			
	def mutatev2(self,mutate_rate):
		x = random.random()
		if x < mutate_rate:
			y = random.random()
			while y < 1:
				node1 = random.choice(self.genome)
				i1 = self.genome.index(node1)
				self.genome.remove(node1)
				node2 = random.choice(self.genome)
				while node2 == node1: 
					node2 = random.choice(self.genome)
				i2 = self.genome.index(node2)
				self.genome.remove(node2)
				self.genome.insert(i1,node2)
				self.genome.insert(i2,node1)
				y = random.random()*5


def main():
	trvl = Traveler(10)
	for path in trvl.genome:
		print(path)

if __name__ == '__main__':
	main()
