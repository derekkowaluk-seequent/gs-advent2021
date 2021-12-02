# Advent 2021 Day 1
# Derek Kowaluk Dec 1, 2021
# 


import sys
import os


def solve(filename):
	f = None
	try:
		f = open(filename)
	except OSError:
		print("File Error")
		return 0

	increase_count = 0
	decrease_count = 0
	line = f.readline()

	previous = value = 0 + int(line)

	while line:
		value = 0 + int(line)
		if (value > previous):
			print("{} (increased)".format(value))
			increase_count = increase_count + 1
		elif (value < previous):
			print("{} (decreased)".format(value))
			decrease_count = decrease_count + 1
		else:
			print("{} (unchanged)".format(value))
		previous = value
		line = f.readline()

	print(decrease_count)
	return increase_count

def main():
	if len(sys.argv) < 2: 
		print("File Path Required")
		sys.exit()
	filepath = sys.argv[1]

	solution = solve(filepath)
	print("The Solution is {}".format(solution))

if __name__ == '__main__':
	main()