#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

bool isPrime(int _n)
{
	if (_n == 1) return false;
	else if (_n == 2) return true;
	else
	{
		for (int i = 2; i < sqrt(_n) + 1; i++)
		{
			if (_n % i == 0) return false;
		}
	}

	return true;
}

int main(void)
{
	int n, in;
	int cnt = 0;

	cin >> n;

	for (int i = 0; i < n; i++)
	{
		cin >> in;
		if (isPrime(in)) cnt++;
	}

	cout << cnt;
}
