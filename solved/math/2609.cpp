#include <iostream>

using namespace std;

int gcd(int _x, int _y)
{
	if (_x < _y)
	{
		int tmp = _x;
		_x = _y;
		_y = tmp;
	}
	if (_x == _y) return _x;
	else if (_y == 0) return _x;
	else return gcd(_y, _x % _y);
}

int lcm(int _x, int _y)
{
	return _x * (_y / gcd(_x, _y));
}


int main(void)
{
	int x, y;

	cin >> x >> y;

	cout << gcd(x, y) << "\n" << lcm(x, y) << "\n";
}
