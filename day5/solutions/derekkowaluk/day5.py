# Advent 2021 Day 5
# Derek Kowaluk Dec 9, 2021
# 

import sys
import os

def get_example_data():
	return [
		"0,9 -> 5,9",
		"8,0 -> 0,8",
		"9,4 -> 3,4",
		"2,2 -> 2,1",
		"7,0 -> 7,4",
		"6,4 -> 2,0",
		"0,9 -> 2,9",
		"3,4 -> 1,4",
		"0,0 -> 8,8",
		"5,5 -> 8,2"
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
		data.append(line.strip())
		line = f.readline()
	return [0,data]


def extract_point(blob):
	return [int(v) for v in blob.split(',')]


def extract_points(line):
	results = []
	return [extract_point(x) for x in line.split('->')][:2]


def print_line(ldata):
	print("({},{}) ({},{})".format(
	ldata[0][0], ldata[0][1],
	ldata[1][0], ldata[1][1]
	))


def solve_part2(data, showoutput = True):
	return 0

def solve_part1(data, showoutput = True):

	line_data = [extract_points(l) for l in data[:11]]

	for each in line_data:
		print_line(each)



	return 0

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