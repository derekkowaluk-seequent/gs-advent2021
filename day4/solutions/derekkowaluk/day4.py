# Advent 2021 Day 3
# Derek Kowaluk Dec 4, 2021
# 

import sys
import os

def get_example_data():
	return [
		[
			7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1
		],
		[
			"22 13 17 11  0",
			" 8  2 23  4 24",
			"21  9 14 16  7",
			" 6 10  3 18  5",
			" 1 12 20 15 19",
			"",
			" 3 15  0  2 22",
			" 9 18 13 17  5",
			"19  8  7 25 23",
			"20 11 10 24  4",
			"14 21 16 12  6",
			"",
			"14 21 17 24  4",
			"10 16 15  9 19",
			"18  8 23 26 20",
			"22 11 13  6  5",
			" 2  0 12  3  7",
		]
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


	first = data[0].split(',')
	numlist = []
	for val in first:
		numlist.append(int(val))
	return [0,[numlist,data[2:]]]

def get_boards(data):
	current_count = 0
	board_list = []
	current_board = []
	for eachline in data:
		if current_count == 5:
			board_list.append(current_board)
			current_board = []
		row = []
		for eachval in eachline:
			row.append(int(eachval))
		current_board.append(row)
		current_count = current_count + 1
	board_list.append(current_board)
	return board_list



def solve_part2(data, showoutput = True):
	return 0

def solve_part1(data, showoutput = True):
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

	print(data[0])
	print(data[1][:5])

	solution = solve_part1(data, False)
	print("The Solution for part 1 is {}".format(solution))

	solution = solve_part2(data, False)
	print("The Solution for part 2 is {}".format(solution))

if __name__ == '__main__':
	main()