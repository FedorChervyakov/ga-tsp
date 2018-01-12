@author Theodor Chervyakov

# Traveling salesman problem solver

**IMPORTANT:**
requires pygame

**Description:**

This program is designed with a purpose to solve TSP problem using genetic algorithm.

**Individual:** Array of N numbers is a genome, where N is a number of cities.
Each number represents a single city. They are connected in the same 
order as they are in the array.

**Steps:**
1. Generate initial population 
2. Assign fitnesses
3. Select best-berforming individuals 
4. Breed new population
5. Mutate few individuals
(Repeat steps 2-5 until the solution is found)
 
