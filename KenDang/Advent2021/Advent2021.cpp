// Advent2021.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <fstream> 
#include "Day5.h"
#include "Day6.h"
constexpr int MissingValue = -9999999;
#define EQ ==
#define NE !=
#define AND &&
#define OR ||
#define LT <
#define GT >
#define GE >=
#define LE <=

static void Day1A_()
{
	std::ifstream infile("1.txt");

	int prev = MissingValue;
	int curr = MissingValue;
	int count = 0;
	while (infile >> curr)
	{
		if (prev NE MissingValue AND prev LT curr)
		{
			count++;
		}
		prev = curr;
	}

	std::cout << "1A:" << count << "\n";
}

#include <deque>
#include <numeric>
static void Day1B_()
{
	std::ifstream infile("1.txt");
	std::deque<int> values; 
	int count = 0;
	int curr;
	while (infile >> curr)
	{
		values.push_back(curr);
		if (values.size() EQ 4)
		{
			auto sum1 = std::accumulate(values.begin(), values.begin() + 3, 0);

			auto sum2 = std::accumulate(values.begin() + 1, values.end(), 0);
			if (sum1 LT sum2)
			{
				count++;
			}
			values.pop_front();
		}
	}

	std::cout << "1B:" << count << "\n";
}
enum class Direction
{
	Forward, Down, Up
};
static Direction AsDirection_(const std::string& s)
{
	if (s EQ "forward") return Direction::Forward;
	if (s EQ "down") return Direction::Down;
	if (s EQ "up") return Direction::Up;
	_ASSERT(false);
	return Direction::Forward;
}
static void Day2A_()
{
	std::ifstream infile("2.txt");
	std::string command;
	int curr;
	int x = 0;
	int y = 0;

	while (infile >> command >> curr)
	{
		switch (AsDirection_(command))
		{
			case Direction::Forward: x += curr; break;
			case Direction::Down: y += curr; break;
			case Direction::Up: y -= curr; break;
		}
	}

	std::cout << "2A:" << x*y << "\n";
}


static void Day2B_()
{
	std::ifstream infile("2.txt");
	std::string command;
	int curr;
	int aim = 0;
	int x = 0;
	int y = 0;

	while (infile >> command >> curr)
	{
		switch (AsDirection_(command))
		{
		case Direction::Forward: 
		{
			x += curr; 
			y += (aim * curr);
			break;
		}
		case Direction::Down: aim += curr; break;
		case Direction::Up: aim -= curr; break;
		}
	}
	std::cout << "2B:" << x * y << "\n";
}
#include <bitset>
#include <vector>
static void Day3A_()
{
	std::ifstream infile("3.txt");
	std::bitset<12> currBitset;
	std::vector<int> binaryCount(12);
	while (infile >> currBitset)
	{
		for (unsigned i = 0; i < currBitset.size(); ++i)
		{
			currBitset.test(i) ? binaryCount[i]++ : binaryCount[i]--;
		}
	}

	std::bitset<12> gamma;
	for (unsigned i = 0; i < binaryCount.size(); ++i)
	{
		gamma.set(i, binaryCount[i] GT 0);
	}
	auto epsilon = ~gamma;

	std::cout << "3A:" << gamma.to_ulong() * epsilon.to_ulong() << "\n";
}

using Bitset = std::bitset<12>;
bool MajoritySet_(int index, const std::vector<Bitset>& list)
{
	int count = 0;
	for (const auto& currBitset : list)
	{
		currBitset.test(index) ? count++ : count--;
	}
	return count GE 0;
}
#include <functional>
using ComparisonFunc = std::function<bool(bool, bool)>;
int FilteredValue_(std::vector<Bitset> list, //copied list since it is modified. HOWEVER, could use std::partition instead of erase_if
	const ComparisonFunc& func)
{
	for (unsigned index = 11; list.size() GT 1 AND index GE 0; --index)
	{
		bool isSet = MajoritySet_(index, list);
		std::erase_if(list, [&](const Bitset& bit) {return func(bit.test(index), isSet); });
	}
	_ASSERT(list.size() EQ 1);
	return list.front().to_ulong();
}

static void Day3B_()
{
	/*
	In string form:
	100000101101
	^          ^
	11th       0th exponent

	In bitset,
	101101000001
	^          ^
	0th	       11th exponent
	*/
	std::vector<Bitset> list;
	std::ifstream infile("3.txt");
	Bitset currBitset;
	while (infile >> currBitset)
	{
		list.push_back(currBitset);
	}
	auto first = FilteredValue_(list, [](const bool b1, const bool b2) {return b1 NE b2; }); //Erase things NOT matching majority
	auto second = FilteredValue_(list, [](const bool b1, const bool b2) {return b1 EQ b2; }); //Erase things matching majority.
	std::cout << "3B:" << first * second << "\n";
}

#include <string>
#include <sstream>
class BingoBoard
{
public:
	BingoBoard(std::vector<std::string>::iterator begin, std::vector<std::string>::iterator end)
	{
		_ASSERT(std::distance(begin, end) EQ 5);
		for (; begin NE end; ++begin)
		{
			std::istringstream iss(*begin);
			std::string subString;
			while (std::getline(iss, subString, ' '))
			{
				if(!subString.empty())
					numbers_.push_back(std::stoi(subString));
			}
		}
		_ASSERT(numbers_.size() EQ 25);
	}
	bool Validate(int number)
	{
		auto itFound = std::find(numbers_.begin(), numbers_.end(), number);
		if (itFound NE numbers_.end())
		{
			auto pos = std::distance(numbers_.begin(), itFound);
			calledFields_.set(pos);
		}
		static const auto winnerBitsets = WinningBitsets_();
		for (const auto& winningBits : winnerBitsets)
		{
			auto won = (winningBits & calledFields_) EQ winningBits;
			if(won)
			{
				return true;
			}
		}
		return false;
	}
	int SumOfUncalled() const
	{
		int sum = 0;
		for (unsigned i = 0; i < 25; ++i)
		{
			if (!calledFields_.test(i))
			{
				sum+=numbers_[i];
			}
		}
		return sum;
	}
private:
	std::vector< std::bitset<25>> WinningBitsets_()
	{
		std::vector< std::bitset<25>> winningBitsets;
		std::string horizString = "1111100000000000000000000"; //represents matches on top row.
		for (unsigned i = 0; i < 5; ++i)
		{
			winningBitsets.emplace_back(horizString);
			std::rotate(horizString.begin(), horizString.begin() + 5, horizString.end()); //rotate 5 times for each row
		}
		std::string vertString = "1000010000100001000010000"; //represents matches on a vert column
		for (unsigned i = 0; i < 5; ++i)
		{
			winningBitsets.emplace_back(vertString);
			std::rotate(vertString.begin(), vertString.begin() + 1, vertString.end()); //Rotate 1 for each column
		}
		return winningBitsets;
	}
	std::bitset<25> calledFields_;
	std::vector<int> numbers_;
};
std::pair<std::vector<int>, std::vector<BingoBoard>> ReadBoard_()
{
	std::vector<int> callingNumbers;
	std::ifstream infile("4.txt");
	std::string line;
	std::vector<std::string> lines;
	while (std::getline(infile, line, '\n'))
	{
		lines.push_back(line);
	}

	std::istringstream iss(lines[0]);
	std::string subString;
	while (std::getline(iss, subString, ','))
	{
		callingNumbers.push_back(std::stoi(subString));
	}
	
	std::vector<BingoBoard> boards;
	for (auto begin = lines.begin() + 2; begin NE lines.end(); std::advance(begin, 6))
	{
		auto end = begin + 5;
		boards.emplace_back(begin, end);
		if (end EQ lines.end()) break;
	}
	return std::make_pair(callingNumbers, boards);
}
static void Day4A_()
{
	auto [callingNumbers, bingoBoards] = ReadBoard_();

	for (const auto number : callingNumbers)
	{
		for (auto& board : bingoBoards)
		{
			if (board.Validate(number))
			{
				std::cout << "4A:" << board.SumOfUncalled() * number << "\n";
				return;
			}
		}
	}
}
static void Day4B_()
{
	auto [callingNumbers, bingoBoards] = ReadBoard_();
	std::vector<bool> winningBoard(bingoBoards.size(), 0);
	auto lastWinningNumber = 0;
	for (const auto number : callingNumbers)
	{
		for (unsigned i = 0; i< bingoBoards.size(); ++i)
		{
			if (!winningBoard[i] AND bingoBoards[i].Validate(number))
			{
				winningBoard[i] = true;
				lastWinningNumber = bingoBoards[i].SumOfUncalled() * number;
			}
		}
	}
	std::cout << "4B:" << lastWinningNumber << "\n";
}
int main()
{
	Day1A_();
	Day1B_();
	Day2A_();
	Day2B_();
	Day3A_();
	Day3B_();
	Day4A_();
	Day4B_();
	day5::A();
	day5::B();
	day6::Run();
}

