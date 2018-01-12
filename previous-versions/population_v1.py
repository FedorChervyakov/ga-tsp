import math
import random
from individual import Traveler
	
class Population:

	pop_size = 0
	genome_len = 0
	cities = []
	
	population = [] 	

	# size is the size of population 
	# nodes is an array of cities 
	def __init__(self, size, nodes):
		self.pop_size = size
		self.cities = nodes
		self.genome_len = len(self.cities)
		self.population = []
		print(self.cities)
		print(self.genome_len)
		i = 0
		while i != self.pop_size:
			tourist = Traveler(self.genome_len)
			self.population.append(tourist)
			self.fitness(tourist)
			i += 1

	def fitness(self,individ):
		fitn = 0
		for pair in individ.genome:
			dx = self.cities[pair[0]][0] - self.cities[pair[1]][0]
			dy = self.cities[pair[0]][1] - self.cities[pair[1]][1]
			fitn += math.sqrt(math.pow(dx,2) + math.pow(dy,2))
		fitn = 1 / fitn 
		individ.fitness = fitn
		return fitn


	def roulette_selection(self):
		# Sum all fitnesses
		fit_sum = 0
		for individ in self.population:
			fit_sum += individ.fitness
		# Generate adjusted fitnesses; adj = fitn/fit_sum
		for individ in self.population:
			individ.adjusted_fitn = individ.fitness / fit_sum
		# Create a tuple list of (cumulative fitness + adjusted fitness, individ)
		cumulative = 0
		selection = []
		for individ in self.population:
			cumulative += individ.adjusted_fitn
			selection.append((cumulative,individ))
		# Select individuals using roulette selection
		i = 0
		candidates = []
		while i != self.size:
			# roulette wheel selection (not optimmized)
			j = 0
			done = False
			rand = random.random()
			while not done:
				if j == 0:
					cuml = 0
				else:
					cuml = selection[j-1][0]
				if (rand <= selection[j][0]) and (rand > cuml):
					candidates.append(selection[j][1])
					done = True
				j += 1
			i += 1
		return candidates

def main():
	tourists = Population(30,[(2,3),(2,5),(10,5),(10,25),(30,10),(20,5)])
	for tour in tourists.population:
		print(tour.genome,tour.fitness)

if __name__ == '__main__':
	main()