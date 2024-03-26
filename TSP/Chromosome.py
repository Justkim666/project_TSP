import math

# class city
class city:
	def __init__(self, name, x, y):
		self.name = int(name)
		self.x = float(x)
		self.y = float(y)

# open file
# total number of city
N = 20
file_name = "training_dataset"
city_list = []

with open(file_name, "r") as f:
	for line in f:
		# remove spaces at the begining and the end
		line = line.strip()
		# split a string into a list, EX: a = ['a','b','c']
		line = line.split(" ")
		name, x, y = line[0], line[1], line[2]
		# create object city and add to dataset
		obj_city = city(name=name, x=x, y=y)
		city_list.append(obj_city)

# create 2D array and contain distance between 2 city
def create_distance_city_matrix(city_list):
	# initial with value 0 for distances without calculate yet
	matrix = [[0 for y in range(N)] for x in range(N)]
	# let calculate euclidean distance
	# a^2 = b^2 + c^2
	for i in range(0, len(city_list)-1):
		for j in range(0, len(city_list)-1):
			matrix[city_list[i].name][city_list[j].name] = math.sqrt(
				pow((city_list[i].x) - (city_list[j].x), 2) + 
				pow((city_list[i].y) - (city_list[j].y), 2) 
			)
	return matrix

# class chromosome
class Chromosome:
	def __init__(self, city_list):
		self.chromosome = city_list
		# just only hold the name of the city so that help get total distance from chomosome
		chr_representation = []
		for i in range(0, len(city_list)-1):
			chr_representation.append(self.chromosome[i].name)
		self.chr_representation = chr_representation
		# get distances from the matrix
		distance = 0
		for i in range(1, len(self.chr_representation)):
			distance += matrix[self.chr_representation[j]-1][self.chr_representation[j+1]-1]
		self.cost = distance
		# fitness value, we need shortest rout
		self.fitness = 1 / self.cost
