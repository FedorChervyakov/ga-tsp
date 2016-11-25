import sys
import pygame
from population import Population
from individual import Traveler
pygame.init()

mutation_rate = 0.4
crossover_point = 0.3
crossover_point2 = 0.7 
#pop_size = 50

size = (960,960)
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)

screen = pygame.display.set_mode(size)


def draw_path(pane,color,Tourist,cities,width=2):
	genome = Tourist.genome
	i = 0
	while i != len(genome):
		start = cities[genome[i-1]]
		end = cities[genome[i]]
		pygame.draw.line(pane, color, start,end, width)
		screen.blit(pane,(0,0))
		i += 1

def read_cities(pane):
	cities = []
	done = False
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				cities.append(pygame.mouse.get_pos())
				pygame.draw.circle(pane, GREEN, pygame.mouse.get_pos(), 7)
				screen.blit(pane,(0,0))
				pygame.display.flip()
			if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_RETURN): done = True
			if event.type == pygame.QUIT: sys.exit()
	return cities

def main():
	pane = pygame.Surface(size)
	pane.fill(WHITE)
	screen.fill(WHITE)
	pygame.display.flip()
	cities = read_cities(pane)
	pop_size = math.pow(2,len(cities)) 		
	pop = Population(pop_size, cities, crossover_point,crossover_point2,mutation_rate)
	done = False
	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
		#pygame.time.Clock().tick(3000)
		pane.fill(WHITE)
		fitn = 0
		for point in cities:
			pygame.draw.circle(pane, GREEN, point, 7)
		draw_path(pane,RED,pop.best_perf,cities,6)
		draw_path(pane,BLACK,pop.best_now,cities)
		pop.evolve()
		screen.blit(pane, (0,0))
		pygame.display.flip()

if __name__ == '__main__':
	main()
