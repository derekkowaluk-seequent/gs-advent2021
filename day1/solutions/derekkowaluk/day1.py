# Advent 2021 Day 1
# Derek Kowaluk Dec 1, 2021
# 


import sys
import os


def get_example_data():
	return [
		199,
		200,
		208,
		210,
		200,
		207,
		240,
		269,
		260,
		263
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
		value = 0 + int(line)
		data.append(value)
		line = f.readline()
	return [0,data]


def solve_part2(data):
	if len(data) < 3 : return 0
	increase_count = 0
	decrease_count = 0

	remove_index = 0
	index = 2

	previous = 0
	eachvalue = data[0] + data[1]
	first = True
	while index < len(data):
		eachvalue = eachvalue + data[index]
		if first: 
			print("{} (N/A - no previous sum)".format(eachvalue))
			first = False
		else:
			if (eachvalue > previous):
				print("{} (increased)".format(eachvalue))
				increase_count = increase_count + 1
			elif (eachvalue < previous):
				print("{} (decreased)".format(eachvalue))
				decrease_count = decrease_count + 1
			else:
				print("{} (no change)".format(eachvalue))
		previous = eachvalue
		eachvalue = eachvalue - data[remove_index]
		remove_index = remove_index + 1
		index = index + 1

	return increase_count


def solve_part1(data):
	increase_count = 0
	decrease_count = 0
	previous = 0
	first = True

	for eachvalue in data:
		if first: 
			print("(N/A - no previous measurement)")
			first = False
		else:
			if (eachvalue > previous):
				print("{} (increased)".format(eachvalue))
				increase_count = increase_count + 1
			elif (eachvalue < previous):
				print("{} (decreased)".format(eachvalue))
				decrease_count = decrease_count + 1
			else:
				print("{} (no change)".format(eachvalue))
		previous = eachvalue

	print(decrease_count)
	return increase_count

def main():
	if len(sys.argv) < 2: 
		print("File Path Required")
		sys.exit()
	filepath = sys.argv[1]

	result,data = get_data(filepath)

	data = get_example_data()

	if result : return

	solution = solve_part1(data)
	print("The Solution for part 1 is {}".format(solution))

	solution = solve_part2(data)
	print("The Solution for part 2 is {}".format(solution))

if __name__ == '__main__':
	main()