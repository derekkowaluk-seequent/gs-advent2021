# Advent 2021 Day 3
# Derek Kowaluk Dec 4, 2021
# 

import sys
import os

def get_example_data():
	return [3,4,3,1,2]

def get_data(filename):
	f = None
	data = []
	try:
		f = open(filename)
	except OSError:
		print("File Error")
		return [-1, data]

	lines = []
	line = f.readline()
	while line:
		lines.append(line.strip())
		line = f.readline()

	data = [int(v) for v in lines[0].split(',')]

	return [0,data]


def solve_part2(data, showoutput = True):

	return 0

def solve_part1(data, showoutput = True):
	print("Initial state:{}".format(data))

	days = 80
	spawncycle = 7

	childcycle = 2

	for day in range(1, days+1):
		newdata = []
		for eachone in data:
			if eachone == 0 : 
				eachone = spawncycle - 1
				newdata.append(eachone)
				newdata.append(spawncycle + childcycle - 1)
			else :
				eachone = eachone - 1
				newdata.append(eachone)
		data = newdata

		if showoutput : print("After {} day{}: {}".format(day, "s" if day > 1 else "", data))

	

	return len(data)
def main():
	data = None
	if len(sys.argv) < 2: 
		print("Using Example Data")
		print("------------------")
		data = get_example_data()
	else:
		filepath = sys.argv[1]
		print("Using file:{}".format(filepath))
		result,data = get_data(filepath)
		if result : 
			sys.exit()

	solution = solve_part1(data, False)
	print("The Solution for part 1 is {}".format(solution))

	solution = solve_part2(data, False)
	print("The Solution for part 2 is {}".format(solution))

if __name__ == '__main__':
	main()