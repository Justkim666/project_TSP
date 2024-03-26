import GeneticAlgorithm as GA
import Chromosome as Ch

# libraries for graphs
import numpy as np
import matplotlib.pyplot as plt

# parameters
number_of_generations = 200
population_size = 100
mut_rate = 0.2
dataset = Ch.city_list

# main function for genetic algorithm
def genetic_algorithm(number_of_generations, pop_size, mutation_rate, data_list):
	# first generation create with initialization function
	new_gen = GA.initialization(data_list, pop_size)
	# show cost through number of generations, y-asix
	cost_graph = []
	for x in range(0, number_of_generations):
		# create ne generation
		new_gen = GA.create_new_generation(new_gen, mutation_rate)
		# print the cost of first chromosome of each new generation to observe the change over generations
		print(str(x) + ". generation --> " + "cost: "+ str(new_gen[0].cost))
		# append the best chromosome's cost of each generation (y-axis)
		cost_graph.append(GA.find_best(new_gen).cost)
		# print the best way
	return new_gen, cost_graph

def draw_cost_generation(y_list):
	x_list = np.arrange(1, len(y_list)+1)
	plt.plot(x_list, y_list)
	plt.title("Route Cost through Generations")
	plt.xlabel("Generations")
	plt.ylabel("Cost")
	plt.show()

def draw_path(solution):
    x_list = []
    y_list = []

    for m in range(0, len(solution.chromosome)):
        x_list.append(solution.chromosome[m].x)
        y_list.append(solution.chromosome[m].y)

    fig, ax = plt.subplots()
    plt.scatter(x_list, y_list)  # alpha=0.5

    ax.plot(x_list, y_list, '--', lw=2, color='black', ms=10)
    ax.set_xlim(0, 1650)
    ax.set_ylim(0, 1300)

    plt.show()


last_generation, y_axis = genetic_algorithm(
    num_of_generations=numbers_of_generations, pop_size=population_size, mutation_rate=mut_rate, data_list=dataset
)

best_solution = GA.find_best(last_generation)

draw_cost_generation(y_axis)

draw_path(best_solution)