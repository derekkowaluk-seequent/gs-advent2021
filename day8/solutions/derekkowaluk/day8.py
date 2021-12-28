# Advent 2021 Day 8
# Derek Kowaluk Dec 21, 2021
# 

import sys
import os

def get_example_data():
	return """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb |fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec |fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf |cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd |ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg |gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc |fgae cfgab fg bagce"""



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

def process_input(data):
	print("Processing...")
	
	#[print(line.split('|')) for line in data]

	sample = []
	output = []
	for eachline in data:
		s, o = eachline.split('|')
		sample.append(s)
		output.append(o)
	return [sample,output]


def solve_part2(data, showoutput = True):
	digit_segments = {0:6,1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6 }

	digits = {
	0:"abcefg",
	1:"cf",
	2:"acdeg",
	3:"acdfg",
	4:"bcdf",
	5:"abdfg",
	6:"abdefg",
	7:"acf",
	8:"abcdefg",
	9:"abcdfg"
	}



	return 0




def solve_part1(data, showoutput = True):
	#print("sample:{}".format(data[0]))

	if showoutput: print("Output:{}".format(data[1]))

	digit_segments = {0:6,1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6 }
	if showoutput: print(digit_segments)
	usedata = data[1]

	cdict = dict.fromkeys(range(1,8),0)
	if showoutput: print(cdict)
	for eachset in usedata:
		for eachone in eachset.split():
			cdict[len(eachone)] += 1
			if showoutput: print("{}".format(len(eachone)), end=' ')
		if showoutput: print()
	if showoutput: print(cdict)

	result = 0
	for eachone in [1, 4, 7, 8]:
		result += cdict[digit_segments[eachone]]

	return result

def main():
	data = None
	if len(sys.argv) < 2: 
		print("Using Example Data")
		print("------------------")
		data = get_example_data().splitlines()
	else:
		filepath = sys.argv[1]
		print("Using file:{}".format(filepath))
		result,data = get_data(filepath)
		if result : 
			sys.exit()

	print("Data Size:{}".format(len(data)))
	pdata = process_input(data)


	solution = solve_part1(pdata, False)
	print("The Solution for part 1 is {}".format(solution))

	solution = solve_part2(pdata, False)
	print("The Solution for part 2 is {}".format(solution))

if __name__ == '__main__':
	main()