#include <iostream>

using namespace std;

int main(void)
{
	int lenth, str;
	int output = 0;

	cin >> lenth;
	int* arr = new int[lenth];

	for (int i = 0; i < lenth; i++)
	{
		cin >> str;
		arr[i] = str;
	}

	cin >> str;
	for (int i = 0; i < lenth; i++)
	{
		if (arr[i] == str) output++;
	}
	
	cout << output;
}
