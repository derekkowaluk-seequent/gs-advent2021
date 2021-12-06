# Advent 2021 Day 3
# Derek Kowaluk Dec 4, 2021
# 

import sys
import os

def get_example_data():
	return [
		"00100",
		"11110",
		"10110",
		"10111",
		"10101",
		"01111",
		"00111",
		"11100",
		"10000",
		"11001",
		"00010",
		"01010"
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


def filter_data(data, filter, compare):
	a_data = []
	b_data = []
	for eachdata in data:
		if filter(eachdata): a_data.append(eachdata)
		else: b_data.append(eachdata)

	if compare(a_data,b_data):
		return a_data
	return b_data

def solve_part2(data, showoutput = True):
	gamma = 0
	epsilon = 0

	oxy_data = data.copy()
	pos = 0
	while len(oxy_data) > 1:
		oxy_data = filter_data(oxy_data, lambda v:v[pos] == '1', lambda a, b: len(a) >= len(b))
		print(oxy_data)

	


	#co2_data = filter_data(data, lambda v:v[0] == '1', lambda a, b: len(a) <= len(b))
	#print(co2_data)



	return gamma * epsilon

def solve_part1(data, showoutput = True):
	gamma = 0
	epsilon = 0
	results = []
	longest = 0
	for val in range(32): results.append(0) 
	for eachvalue in data:
		pos = 0
		for eachbit in eachvalue:
			if int(eachbit) == 0: results[pos] = results[pos] - 1
			else : results[pos] = results[pos] + 1
			pos = pos + 1
			if pos > longest : longest = pos

	gammastr = ""
	epsilonstr = ""

	for index in range(longest):
		gamma = gamma << 1
		epsilon = epsilon << 1

		if results[index] > 0 : 
			gammastr = gammastr + '1'
			epsilonstr = epsilonstr + '0'
			gamma = gamma + 1
		else : 
			gammastr = gammastr + '0'
			epsilonstr = epsilonstr + '1'
			epsilon = epsilon + 1



	print("{}:{}".format(gammastr, gamma))
	print("{}:{}".format(epsilonstr, epsilon))


	return gamma * epsilon

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