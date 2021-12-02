# Advent 2021 Day 1
# Derek Kowaluk Dec 1, 2021
# 


import sys
import os


def solve(filename):
	f = open(filename, 'rU')
	line = f.readline()
	while line:
		print(line)



def main():
	if len(sys.argv) < 2: 
		print("File Path Required")
		sys.exit()
	filepath = sys.argv[1]

	solution = 0
	print("The Solution is {}".format(solution))

if __name__ == '__main__':
	main()