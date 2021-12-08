# Advent 2021 Day 7
# Derek Kowaluk Dec 7, 2021
# 

import sys
import os

class rolling_mean:
	mean = 0
	accum_positive = 0
	accum_negative = 0
	count = 0

	def __str__(self):
		return "Mean:{} +:{} -:{} ({})".format(self.mean, self.accum_positive, self.accum_negative, self.count)


	def add_value(self, value):
		if not self.count  :
			self.mean = value
			self.count = 1
			return self.mean

		left = self.accum_positive
		right = self.accum_negative

		self.count = self.count + 1

		if value > self.mean:
			left = left + value - self.mean

			if right > left:
				right = right - left
				left = 0
			else :
				left = left - right
				right = 0
				while left >= self.count:
					self.mean = self.mean + 1
					left = left - self.count
		else:
			right = right + self.mean - value

			if left > right:
				left = left - right
				right = 0
			else :
				right = right - left
				left = 0
				while right >= self.count:
					self.mean = self.mean - 1
					right = right - self.count

		self.accum_positive = left
		self.accum_negative = right
		return self.mean


def get_example_data():
	return [ 16,1,2,0,4,2,7,1,2,14 ]



def get_data(filename):
	f = None
	data = []
	try:
		f = open(filename)
	except OSError:
		print("File Error")
		return [-1, data]

	line = f.readline()
	strdata = line.strip().split(',')
	for each in strdata:
		data.append(int(each))

	return [0,data]


def solve_part2(data, showoutput = True):

	return 0
def solve_part1(data, showoutput = True):
	rm = rolling_mean()
	for each in data:
		print("Add:{}".format(each))
		rm.add_value(each)
		print(rm)

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

	print("Data Size:{}".format(len(data)))

	solution = solve_part1(data, False)
	print("The Solution for part 1 is {}".format(solution))

	solution = solve_part2(data, False)
	print("The Solution for part 2 is {}".format(solution))

if __name__ == '__main__':
	main()