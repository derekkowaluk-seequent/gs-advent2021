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


def solve_part2(data, showoutput = True):
	hpos = 0
	dpos = 0
	aim = 0
	for eachvalue in data:
		command, value = eachvalue.split()
		intvalue = int(value)
		if command == 'forward':
			hpos = hpos + intvalue
			dpos = dpos + aim * intvalue
		elif command == 'down':
			aim = aim + intvalue
		elif command == 'up':
			aim = aim - intvalue
		if showoutput: print("{} {}: hpos={} dpos={} aim={}".format(command, value,hpos,dpos,aim))

	return hpos * dpos

def solve_part1(data, showoutput = True):
	hpos = 0
	dpos = 0
	for eachvalue in data:
		command, value = eachvalue.split()
		if showoutput: print("{} {}".format(command, value))
		intvalue = int(value)
		if command == 'forward':
			hpos = hpos + intvalue
		elif command == 'down':
			dpos = dpos + intvalue
		elif command == 'up':
			dpos = dpos - intvalue

	return hpos * dpos

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

	solution = solve_part2(data)
	print("The Solution for part 2 is {}".format(solution))

if __name__ == '__main__':
	main()