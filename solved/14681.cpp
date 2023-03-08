#include <iostream>

using namespace std;

int main(void)
{
	int x, y;
	int output = 1;
	cin >> x >> y;
	
	if (x < 0)
	{
		if (y > 0) output = 2;
		else output = 3;
	}
	else
	{
		if (y < 0) output = 4;	
	}
	cout << output;
}
