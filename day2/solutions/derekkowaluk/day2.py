# Advent 2021 Day 2
# Derek Kowaluk Dec 4, 2021
# 

import sys
import os

def get_example_data():
	return [
		"forward 5",
		"down 5",
		"forward 8",
		"up 3",
		"down 8",
		"forward 2"
		]

def get_data(filename):
	f = None
	data = []
	try:
		f = open(filename)
	except OSError:
		print("File Error")
		return [-1, data]

	line = f.readline()
	while line:
		data.append(line)
		line = f.readline()
	return [0,data]


def solve_part2(data):
	return 0

def solve_part1(data):
	return 0

def main():
	data = None
	if len(sys.argv) < 2: 
		print("Using Example Data")
		data = get_example_data()
	else:
		filepath = sys.argv[1]
		result,data = get_data(filepath)
		if result : 
			sys.exit()

	solution = solve_part1(data)
	print("The Solution for part 1 is {}".format(solution))

	solution = solve_part2(data)
	print("The Solution for part 2 is {}".format(solution))

if __name__ == '__main__':
	main()