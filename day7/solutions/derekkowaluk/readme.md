###Explaination

Input:

16,1,2,0,4,2,7,1,2,14


FuelUsed = |16 - x| + |1 - x| + |2 - x| + |0 - x| + |4 - x| + |2 - x| + |7 - x| + |1 - x| + |2 -  x| + |14 - x|

Sorted:
FuelUsed = |0 -  x| + |1 - x| + |1 - x| + |2 - x| + |2 - x| + |2 - x| + |4 - x| + |7 - x| + |14 - x| + |16 - x|  

					^ Imagine Checking Here																
			(x - 0)	+ (x - 1)	(x - 1)	<-> (2 - x) + (2 - x) ....  
				Each  is (x - N) before the check point and (N - x) after				

Algorithm:

Sort into buckets

add each to the Total = 49
Count of Input = 10

sort the buckets, each number below is the count inside
`0  1  2  4  7 14 16`
`1  2  3  1  1  1  1`

now traverse them starting at 0

0:
CountBehind = 1
TotalBehind = 0 x 1
TotalAhead = 49 - TotalBehind = 49
CountAhead = Count - CountBehind = 9
FuelUsed = (TotalAhead - 0 x CountAhead) + (0 x CountBehind - TotalBehind) = 49

1:
CountBehind = CountBehind + 2 = 3
TotalBehind = TotalBehind + 1 x 2 = 2
TotalAhead = Total - TotalBehind = 47
CountAhead = Count - CountBehind = 7
FuelUsed = (TotalAhead - 1 x CountAhead) + (1 x CountBehind - TotalBehind)
	     = ( 47 - 1 x 7) + (1 x 3 - 2) = 41

2:
CountBehind = CountBehind + 3 = 6
TotalBehind = TotalBehind + 2 x 3 = 8
TotalAhead = Total - TotalBehind = 41
CountAhead = Count - CountBehind = 4
FuelUsed = (TotalAhead - 2 x CountAhead) + (2 x CountBehind - TotalBehind)
	     = ( 41 - 2 x 4) + (2 x 6 - 8) = 37


And so on


