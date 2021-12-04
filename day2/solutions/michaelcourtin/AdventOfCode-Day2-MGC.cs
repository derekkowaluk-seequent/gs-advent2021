public void SubTest()
{
	var subData =  new List<(string Direction, int Magnitude)>();
	//read input file
	foreach (string line in System.IO.File.ReadLines(@"d:\Michael\input.txt"))
	{
		string[] data = line.Split(' ');
		string direction = data[0];
		int magnitude = int.Parse(data[1]);
		var t = (direction, magnitude);
		subData.Add(t);
	}

	//Puzzle #1
	int depth_1 = 0;
	int horizontal_1 = 0;
	int final_answer = 0;
	foreach (var item in subData)
	{
		if (item.Direction == "forward")
		{
			horizontal_1 += item.Magnitude;
		}
		else if (item.Direction == "down")
		{
			depth_1 += item.Magnitude;
		}
		else if (item.Direction == "up")
		{
			depth_1 -= item.Magnitude;
		}
	}
	final_answer = horizontal_1 * depth_1;
	MessageBox.Show(final_answer.ToString(), "Puzzle #1");

	//Puzzle #2
	int depth_2 = 0;
	int horizontal_2 = 0;
	int aim = 0;
	int final_answer_2 = 0;
	foreach (var item in subData)
	{
		if (item.Direction == "forward")
		{
			horizontal_2 += item.Magnitude;
			depth_2 += aim * item.Magnitude;
		}
		else if (item.Direction == "down")
		{
			aim += item.Magnitude;
		}
		else if (item.Direction == "up")
		{
			aim -= item.Magnitude;
		}
	}
	final_answer_2 = horizontal_2 * depth_2;
	MessageBox.Show(final_answer_2.ToString(), "Puzzle #2");
}