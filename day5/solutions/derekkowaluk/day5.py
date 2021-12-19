# Advent 2021 Day 5
# Derek Kowaluk Dec 9, 2021
# 

import sys
import os

from PIL import Image

class memory:
	def __init__(self, xsize,ysize):
		self.mem = [0] * xsize * ysize
		self.xsize = xsize
		self.ysize = ysize

	def __str__(self):
		return "Mem:{}x{} ({})".format(self.xsize, self.ysize, len(self.mem))

def get_example_data():
	return [
		"0,9 -> 5,9",
		"8,0 -> 0,8",
		"9,4 -> 3,4",
		"2,2 -> 2,1",
		"7,0 -> 7,4",
		"6,4 -> 2,0",
		"0,9 -> 2,9",
		"3,4 -> 1,4",
		"0,0 -> 8,8",
		"5,5 -> 8,2"
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


def extract_point(blob):
	return [int(v) for v in blob.split(',')]


def extract_points(line):
	results = []
	return [extract_point(x) for x in line.split('->')][:2]


def print_line(ldata):
	print("({},{}) ({},{})".format(
	ldata[0][0], ldata[0][1],
	ldata[1][0], ldata[1][1]
	))

def get_chart(ldata, xsize = 10, ysize = 10):

	maxx = xsize
	maxy = ysize

	for each in ldata:
		for point in each:
			if point[0] > maxx: maxx = point[0]
			if point[1] > maxy: maxy = point[1]

	print("Creating {} x {} chart".format(maxx,maxy))
	return memory(maxx + 1, maxy + 1)

def draw_rectangle(img, pos, size, color):
	for y in range(size[1]):
		for x in range(size[0]):
			img.putpixel((pos[0] + x, pos [1] + y), color)


def print_chart(mem):
	scale = 1
	if mem.xsize > 40 or mem.ysize > 40:
		print("Large Memory")
	else:
		scale = 100

	newimage = Image.new('RGB', (mem.xsize, mem.ysize))  # type, size

	c = 0
	for x in range(mem.xsize):
		for y in range(mem.ysize):
			v = mem.mem[y * mem.xsize + x]
			c = 10 + v * 50
			if c > 255 : c = 0
			#newimage.putpixel((x,y), (255,c,255))
			draw_rectangle(newimage, (scale * x, scale * y), (scale,scale), (c,c,c))

	newimage.save("filename.png")  # takes type from filename extension
	newimage.show()
	return
	

	for x in range(mem.xsize):
		for y in range(mem.ysize):
			v = mem.mem[x * mem.xsize + y]
			print((str(v) if v else '.'),end='')
		print()
	print()



def draw_point(mem, point):
	#print(point)
	loc = point[1] * mem.xsize + point[0]
	#print(loc)
	mem.mem[loc] = mem.mem[loc] + 1

def draw_line(mem, line):
	#print(line)
	dx = line[1][0] - line[0][0]
	dy = line[1][1] - line[0][1]
	#print("dx:{} dy{}".format(dx,dy))
	x0, y0 = line[0]
	xstep = 1 if dx >= 0 else -1
	ystep = 1 if dy >= 0 else -1
	mx = abs(dx)
	my = abs(dy)
	yaccum = 0
	ny = 0

	if mx == 0 :
		for y in range(y0, y0 + dy + ystep, ystep):
			draw_point(mem, [x0,y])
	else:
		for x in range(x0, x0+dx+xstep,xstep):
			draw_point(mem, [x,y0 + ny])
			yaccum = yaccum + my
			while yaccum >= mx:
				ny = ny + ystep
				yaccum = yaccum - mx

def solve_part2(data, showoutput = True):
	return 0

def solve_part1(data, showoutput = True):

	line_data = [extract_points(l) for l in data]

	mem = get_chart(line_data)
	print(mem)

	for each in line_data:
		if each[0][0] == each[1][0] or each[0][1] == each[1][1]:
			draw_line(mem, each)

	overlap_count = 0
	for each in mem.mem:
		if each > 1 : overlap_count = overlap_count + 1

	print_chart(mem)

	return overlap_count

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