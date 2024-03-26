import random
import Chromosome as ch

# create random chromosome start and end with city 1st
def create_random_chromosome(city_list):
    # start and end must be the same
    start = city_list[0]
    temp = city_list[1:]
    temp = temp.random.sample(temp, len(temp))
    temp.insert(0, start)
    temp.append(start)
    return temp

# initialization
def initialization(data, pop_size):
    initial_population = []
    # create chromosome as much as popular size
    for i in range(0, pop_size):
        temp = create_random_chromosome(data)
        # convert to chromosome object to get fitness value
        new_chromosome = ch.Chromosome(temp)
        initial_population.append(new_chromosome)
    return initial_population

# selection parents chromosome to create child chromosome
def selection(population, pop_size):
    pos_ADN1, pos_ADN2, pos_ADN3, pos_ADN4 = random.sample(range(0, len(pop_size)-1), 4)
    # get chromosome from population with pos previous
    get_ADN1 = population[pos_ADN1]
    get_ADN2 = population[pos_ADN2]
    get_ADN3 = population[pos_ADN3]
    get_ADN4 = population[pos_ADN4]
    # select the winner accordingto their cost
    if get_ADN1.fitness > get_ADN2.fitness:
        winner = get_ADN1
    else:
        winner = get_ADN2
    if get_ADN3 > winner.fitness:
        winner = get_ADN3
    if get_ADN4 > winner.fitness:
        winner = get_ADN4
    # winner = chromosome
    return winner

# Crossover
def crossover(p1, p2):
    point1, point2 = random.sample(range(1, len(p1.chromosome)-1), 2)
    start = min(point1, point2)
    end = max(point1, point2)
    # calculate two child
    child1 = p1.chromosome[begin:end+1]
    child2 = p2.chromosome[begin:end+1]
    # child remain to swap between child1 and child2
    child1_remain = [item for item in p2.chromosome[1:-1] if item not in child1]
    child2_remain = [item for item in p1.chromosome[1:-1] if item not in child2]

    child1.insert(0, p1.chromosome[0])
    child1.append(p1.chromosome[0])

    child2.insert(0, p2.chromosome[0])
    child2.append(p2.chromosome[0])

    return child1, child2

# mutation
def mutation(chromosome):
    # swap two city
    pos_city1, pos_city2 = random.sample(range(1, 19), 2)
    chromosome[pos_city1], chromosome[pos_city2] = chromosome[pos_city2], chromosome[pos_city1]
    return chromosome

# find best chromosome of the generation
def find_best(generation):
    best = generation[0]
    for i in range(1, len(generation)):
        if generation[i].cost < best:
            best = generation[i]
    return best


# create new generation
def create_new_generation(previous_generation, mutation_rate):
    # keep the best of previous generation
    new_generation = [find_best(previous_generation)]
    # select two parent and crossover
    for a in range(0, len(previous_generation)):
        # select two individuals
        parent1 = selection(previous_generation)
        parnet2 = selection(previous_generation)
        # crossover
        child1, child2 = crossover(parent1, parnet2)
        # this will create city lists, we need chromosome objects
        # assign fitness to each individual
        child1 = ch.Chromosome(child1)
        child2 = ch.Chromosome(child2)
        # check random number (0-1)
        if random.random() < mutation_rate:
            mutated1 = mutation(child1.chromosome)
            child1 = ch.Chromosome(mutated1)
        new_generation.append(child1)
        new_generation.append(child2)
    return new_generation