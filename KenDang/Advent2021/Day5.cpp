#include "Day5.h"

#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <cmath>
struct Point
{
	int x = 0;
	int y = 0;
};

//returns -1 or 0 or 1
static int IntComp_(int a, int b)
{
	return (b < a) - (a < b) ;
}

class Line
{
public:
	bool IsVertical() const { return p1.y == p2.y; }
	bool IsHorizontal() const { return p1.x == p2.x; }
	std::vector<Point> PointsBetween() const
	{
		std::vector<Point> pts;

		//find direction of x and y
		auto dx = IntComp_(p2.x, p1.x);
		auto dy = IntComp_(p2.y, p1.y); 
		
		for (auto x = p1.x, y = p1.y;
			x != p2.x || y != p2.y;
			x += dx,y += dy)
		{
			pts.emplace_back(x, y);
		}
		pts.emplace_back(p2); //loop didn't include last point. 
		return pts;
	}
	Point p1;
	Point p2;
};

static std::pair<std::vector<Line>, int> ReadLines_()
{
	int maxSize = 0;
	std::ifstream infile("5.txt");
	std::vector<Line> lines;
	Line line;
	std::string filler;
	char c1, c2;
	while (infile >> line.p1.x >> c1 >> line.p1.y >> filler >> line.p2.x >> c2 >> line.p2.y)
	{
		maxSize = std::max({ maxSize, line.p1.x, line.p1.y, line.p2.x, line.p2.y });
		lines.emplace_back(line);
	}
	return std::make_pair(lines, maxSize+1);
}

void day5::A()
{
	auto [lines, maxSize] = ReadLines_();
	std::vector<int> counts; 
	counts.resize(maxSize* maxSize);//1000x1000 = 1,000,000 

	for(const auto& line : lines)
	{
		if (line.IsVertical() || line.IsHorizontal()) //skip diagonal
		{
			for (const auto pt : line.PointsBetween())
			{
				auto index = pt.y * maxSize + pt.x;
				++counts[index];
			}
		}
	}
	std::cout << "5A:" << std::count_if(counts.begin(), counts.end(), [](int i) {return i > 1; }) << "\n";
}

void day5::B()
{
	auto [lines, maxSize] = ReadLines_();
	std::vector<int> counts;
	counts.resize(maxSize * maxSize);//1000x1000 = 1,000,000 

	for (const auto& line : lines)
	{
		for (const auto pt : line.PointsBetween())
		{
			auto index = pt.y * maxSize + pt.x;
			++counts[index];
		}
	}
	std::cout << "5A:" << std::count_if(counts.begin(), counts.end(), [](int i) {return i > 1; }) << "\n";
}