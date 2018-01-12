import math
import random


class Traveler:
	# Single individual

	# Size of genome (number of cities)
	size = 0

	genome = (0,0)

	fitness = 0

	def __init__(self,size,genome):
		self.size = size
		# Initialize new random population
		self.genome = genome
'''
	def __init__(self,size,genome=[]):
		self.size = size
		self.genome = genome
		# Initialize new random population
		i = 0
		ends = []
		while i != size:
			ends.append(i)
			i += 1
		i = 0 
		while i != size:
			start = i
			if len(ends) != 1:
				if start in ends:
					ends.remove(start)
					end = random.choice(ends)
					ends.append(start)
				else:
					end = random.choice(ends)
			else:
				end = ends[0]
			ends.remove(end)
			self.genome.append((start,end))
			i += 1
		# check if last element is (x,x)	
		if self.genome[size-1][0] == self.genome[size-1][1]:
			cand1 = self.genome[size-1]
			self.genome.remove(cand1)
			cand2 = random.choice(self.genome)
			new = (cand1[0],cand2[1])
			self.genome.append(new)
			new2 = (cand2[0],cand1[1])
			index = self.genome.index(cand2)
			self.genome.remove(cand2)
			self.genome.insert(index,new2)
'''

def main():
	trvl = Traveler(10)
	for path in trvl.genome:
		print(path)

if __name__ == '__main__':
	main()
