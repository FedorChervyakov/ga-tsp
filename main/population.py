import math
import random
from individual import Traveler
	
class Population:

	crossover_point = 0
	crossover_point2 = 0
	mutation_rate = 0
	pop_size = 0
	cities = []
	
	population = [] 

	best_perf = Traveler(0)
	top_fit = 0

	best_now = Traveler(0)
	best_fit = 0

	# size is the size of population 
	# nodes is an array of cities 
	def __init__(self, size, nodes, cross_point=0.2,cross_point2=0.6, mutate_rate=0.2):
		self.pop_size = size
		self.cities = nodes
		self.mutation_rate = mutate_rate
		self.crossover_point = int(cross_point * len(self.cities))
		self.crossover_point2 = int(cross_point2 * len(self.cities))
		# Initialize new random population
		i = 0
		while i != self.pop_size:
			new_tourist = Traveler(len(self.cities))
			self.fitness(new_tourist)
			self.population.append(new_tourist)
			new_tourist = None
			i += 1 

	# Simple one-point crossover
	def crossover(self,cand1,cand2):
		i = 0
		new_genome1 = cand1.genome[:self.crossover_point]
		while i != len(cand1.genome):
			if cand2.genome[i] not in new_genome1:
				new_genome1.append(cand2.genome[i])
			i += 1
		res1 = Traveler(len(self.cities),new_genome1)
		self.fitness(res1)		
		return res1

	# Two-point crosover techique
	def two_point_crossover(self,cand1,cand2):
		new_genome1 = [] + cand1.genome[:self.crossover_point]
		i = 0
		while (i != len(cand1.genome)) and (len(new_genome1) != self.crossover_point2):
			if cand2.genome[i] not in new_genome1:
				new_genome1.append(cand2.genome[i])
			i += 1
		i = 0
		while i != len(cand1.genome):
			if cand1.genome[i] not in new_genome1:
				new_genome1.append(cand1.genome[i])
			i += 1
		res1 = Traveler(len(self.cities),new_genome1)
		self.fitness(res1)
		return res1

	def evolve(self):
		candidates = self.roulette_selection()
		new_pop = []
		i = 0 
		while i != self.pop_size:
			cand1 = random.choice(candidates)
			cand2 = random.choice(candidates)
			while cand2 == cand1:
				cand2 = random.choice(candidates)
			new_cand = self.two_point_crossover(cand1,cand2)
			new_pop.append(new_cand)
			i += 1
		for individ in self.population:
			self.population.remove(individ)
		# Perform mutation (see individual.mutate())
		for individ in new_pop: individ.mutate(self.mutation_rate)
		for individ in new_pop:
			self.fitness(individ)
			self.population.append(individ)
		self.best_fit = 0
		self.best_now = Traveler(0)
		for individ in new_pop:
			if individ.fitness > self.top_fit:
				self.top_fit = individ.fitness
				self.best_perf = individ
			if individ.fitness > self.best_fit:
				self.best_fit = individ.fitness
				self.best_now = individ


	def fitness(self,individ):
		fitn = 0
		i = 0
		while i != len(individ.genome):
			dx =  self.cities[individ.genome[i]][0] - self.cities[individ.genome[i-1]][0]
			dy =  self.cities[individ.genome[i]][1] - self.cities[individ.genome[i-1]][1] 
			fitn += 1 / math.sqrt(math.pow(dx,2) + math.pow(dy,2))
			i += 1
		individ.fitness = fitn
		return fitn

	def fitnessv2(self,individ):
		fitn = 0
		i = 0
		while i != len(individ.genome):
			dx =  self.cities[individ.genome[i]][0] - self.cities[individ.genome[i-1]][0]
			dy =  self.cities[individ.genome[i]][1] - self.cities[individ.genome[i-1]][1] 
			fitn += math.sqrt(math.pow(dx,2) + math.pow(dy,2))
			i += 1
		fitn = 1000 / math.pow(10*fitn,5)
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
		while (i != self.pop_size):
			# roulette wheel selection (not optimmized)
			j = 0
			done = False
			rand = random.random()
			while (not done) and (j != len(selection)):
				if j == 0:
					cuml = 0
				else:
					cuml = selection[j-1][0]
				if (rand <= selection[j][0]) and (rand > cuml):
					""" and (selection[j][1] not in selection):"""
					candidates.append(selection[j][1])
					done = True
				j += 1
			i += 1
		return candidates

def main():
	tourists = Population(5,[(2,3),(2,5),(10,5),(10,25),(30,10),(20,5)])
	for tour in tourists.population:
		print(tour.genome,tour.fitness)

if __name__ == '__main__':
	main()