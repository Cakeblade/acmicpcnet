#include <iostream>

using namespace std;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	long n;
	int arr[10001] = {0, };
	int in;

	cin >> n;

	for (int i = 0; i < n; i++) 
	{
		cin >> in;
		arr[in]++;
	}

	for (int i = 1; i < 10001; i++)
	{
		if (arr[i] != 0)
		{
			for (int j = 0; j < arr[i]; j++) cout << i << "\n";
		}
	}
}
