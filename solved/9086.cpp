#include <iostream>
#include <string>

using namespace std;

int main(void)
{
	int n;
	string str;

	cin >> n;

	for (int i = 0; i < n; i++) 
	{
		cin >> str;
		cout << str.at(0) << str.back() << "\n";
	}
	

}
