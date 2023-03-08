#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main(void)
{
	int m, n, w, b;
	int mi = 65;
	string line;

	cin >> n >> m;

	char** chess = new char*[n];
	
	for (int i = 0; i < n; i++) chess[i] = new char[m];

	for (int i = 0; i < n; i++)
	{
		cin >> line;
		for (int j = 0; j < m; j++)
		{
			chess[i][j] = line[j];	
		}
	}

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			cout << chess[i][j];
		}
		cout << "\n";
	}


	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			w = 0;
			b = 0;
			for (int k = 0; k < i + 8; k++)
			{
				for (int l = 0; l < j + 8; l++)
				{
					if ((k + l) % 2 == 0)
					{
						if (chess[k][l] != 'W') w += 1;
						if (chess[k][l] != 'B') b += 1;
					}
					else
					{
						if (chess[k][l] != 'W') b += 1;
						if (chess[k][l] != 'B') w += 1;
					}
				}
			}
			mi = min({mi, w, b});
		}
	}
	
}
