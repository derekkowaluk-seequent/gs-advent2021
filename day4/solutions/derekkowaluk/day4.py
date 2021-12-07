# Advent 2021 Day 3
# Derek Kowaluk Dec 4, 2021
# 

import sys
import os

class GameBoard:
	board = None
	hitcount = 0
	active = True
	def __init__(self, board):
		self.board = board.copy()


	def print_board(self):
		for eachrow in self.board:
			for eachnum in eachrow:
				status = '*' if eachnum[1] else ' '
				print("{:>2}{}".format(eachnum[0], status), end=' ')
			print()

	def add_ball(self, ball):
		current = [0,0]
		for eachrow in self.board:
			current[0] = 0
			for item in eachrow:
				if ball == item[0]:
					item[1] = 1
					self.hitcount = self.hitcount + 1
					return current
				current[0] = current[0] + 1

			current[1] = current[1] + 1
		return [-1,-1]

	def check_ball(self, ball):
		b = self.add_ball(ball)
		if b[0] != -1 : 
			#print(b)
			if self.hitcount > 5:
				if self.check_vertical(b) or self.check_horizontal(b):
					#print("Line Found!!!")
					return True



	def check_horizontal(self, pos):
		column, row = pos
		for eachnum in self.board[row]:
			if not eachnum[1]: return False
		#print("Horizontal")
		return True

	def check_vertical(self, pos):
		column, row = pos
		for eachrow in self.board:
			if not eachrow[column][1]: return False
		#print("Vertical:{}".format(column))
		return True

	def sum_unmarked(self):
		total = 0
		for eachrow in self.board:
			for eachnum in eachrow:
				if not eachnum[1] : total = total + eachnum[0]
		return total


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

def get_boards(data, showoutput = True):
	current_count = 0
	board_list = []
	current_board = []
	for eachline in data:
		if current_count > 4:
			current_count = 0
			if showoutput :
				print(current_board)
				print()
			board_list.append(GameBoard(current_board))
			current_board = []
		row = []

		for eachval in eachline.split():
			row.append([int(eachval), 0])
		if len(row) : 
			current_board.append(row.copy())
			current_count = current_count + 1

		
	board_list.append(GameBoard(current_board))
	if showoutput : print()
	return board_list



def solve_part2(data, showoutput = True):
	boards = get_boards(data[1], showoutput)
	for eachball in data[0][:]:
		if showoutput : print("{}".format(eachball))
		boardcount = 0
		lastboard = None
		for eachboard in boards:
			if not eachboard.active : continue
			boardcount = boardcount + 1
			result = eachboard.check_ball(eachball)
			if showoutput : 
				eachboard.print_board()
				print()
			if result: 
				eachboard.active = False
			#check_ball(eachboard, eachball)
			lastboard = eachboard
		if boardcount == 1 and not lastboard.active:
			if showoutput : 
				print("Last Board:")
				lastboard.print_board()
			return lastboard.sum_unmarked() * eachball

		if showoutput : print("-"*20)
	return 0

def solve_part1(data, showoutput = True):
	boards = get_boards(data[1], showoutput)
	
	for eachball in data[0][:]:
		if showoutput :print("{}".format(eachball))
		for eachboard in boards:
			result = eachboard.check_ball(eachball)
			if showoutput :
				eachboard.print_board()
				print()
			if result: 
				return eachboard.sum_unmarked() * eachball
			#check_ball(eachboard, eachball)
		if showoutput : print("-"*20)

	return 0

def main():
	data = None
	if len(sys.argv) < 2: 
		print("Using Example Data")
		print("-"*40)
		data = get_example_data()
	else:
		filepath = sys.argv[1]
		print("Using file:{}".format(filepath))
		result,data = get_data(filepath)
		if result : 
			sys.exit()

	#print(data[0])
	#print(data[1][:5])

	solution = solve_part1(data, False)
	print("The Solution for part 1 is {}".format(solution))

	solution = solve_part2(data, False)
	print("The Solution for part 2 is {}".format(solution))

if __name__ == '__main__':
	main()