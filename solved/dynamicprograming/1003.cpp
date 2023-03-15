#include <iostream>
#include <vector>

using namespace std;

vector<int> zero;
vector<int> one;

void fibo(int _n)
{
	if (_n >= zero.size())
	{
		for (int i = zero.size(); i <= _n; i++)
		{
			zero.push_back(zero[i - 1] + zero[i - 2]);
			one.push_back(one[i - 1] + one[i - 2]);
		}
	}

	cout << zero[_n] << " " << one[_n] << "\n";
}

int main(void)
{
	int n, input;
	
	zero.push_back(1);
	zero.push_back(0);
	zero.push_back(1);

	one.push_back(0);
	one.push_back(1);
	one.push_back(1);

	cin >> n;

	for (int i = 0; i < n; i++)
	{
		cin >> input;
		fibo(input);
	}

}
