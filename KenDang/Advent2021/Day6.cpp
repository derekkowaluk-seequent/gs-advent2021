#include "Day6.h"
#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <array>
#include <algorithm>
#include <numeric>

auto Run_(auto infile, const unsigned days)
{
	std::string line;
	std::array<unsigned long long, 9> numOfFishPerState = { };
	while (std::getline(infile, line, ','))
	{
		auto fishState = std::stoi(line);
		++numOfFishPerState[fishState];
	}
	for (unsigned i = 0; i < days; ++i)
	{
		auto numGivingBirth = numOfFishPerState[0];
		std::rotate(numOfFishPerState.begin(), numOfFishPerState.begin() + 1, numOfFishPerState.end()); //0 state automatically goes to 9th day 
		numOfFishPerState[6] += numGivingBirth;  //0 state also added to 7th day
	}
	return  std::accumulate(numOfFishPerState.begin(), numOfFishPerState.end(), 0ull);
}

void day6::Run()
{
	_ASSERT(Run_(std::stringstream("3,4,3,1,2"), 80) == 5934);
	_ASSERT(Run_(std::stringstream("3,4,3,1,2"), 256) == 26984457539);
	std::cout << "6A:" << Run_(std::ifstream("6.txt"), 80) << "\n";
	std::cout << "6A:" << Run_(std::ifstream("6.txt"), 256) << "\n";
}
