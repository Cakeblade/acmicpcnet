#include <iostream>

using namespace std;

int main(void)
{
	long n, m;
	cin >> n >> m;
	if (n < m) cout << m - n;
	else cout << n - m;

}
