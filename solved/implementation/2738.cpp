#include <iostream>

using namespace std;

int main(void)
{
	int x, y, str;
	
	cin >> x >> y;
	
	int** m1 = new int*[x];

	for (int i = 0; i < x; i++)
		m1[i] = new int[y];
	

	for (int i = 0; i < x; i++)
	{
		for (int j = 0; j < y; j++)
		{
			cin >> str;
			m1[i][j] = str;
		}
	}

	for (int i = 0; i < x; i++)
	{
		for (int j = 0; j < y; j++)
		{
			cin >> str;
			m1[i][j] = m1[i][j] + str;
		}
	}
	
	for (int i = 0; i < x; i++)
	{
		for (int j = 0; j < y; j++)
		{
			cout << m1[i][j] << " ";
		}
		cout << "\n";
	}
}
