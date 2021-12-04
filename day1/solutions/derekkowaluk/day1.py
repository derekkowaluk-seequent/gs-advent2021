# Advent 2021 Day 1
# Derek Kowaluk Dec 1, 2021
# 


import sys
import os


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


def solve_part2(filename):
	return 0


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
				print("{} (unchanged)".format(eachvalue))
		previous = eachvalue

	print(decrease_count)
	return increase_count

def main():
	if len(sys.argv) < 2: 
		print("File Path Required")
		sys.exit()
	filepath = sys.argv[1]

	result,data = get_data(filepath)

	if result : return

	solution = solve_part1(data)
	print("The Solution is {}".format(solution))

if __name__ == '__main__':
	main()