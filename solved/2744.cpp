#include <iostream>
#include <string>

using namespace std;

int main(void)
{
	string str;
	cin >> str;
	for (unsigned long i = 0; i < str.size(); i++) 
	{
		if (str[i] >= 'a') str[i] = toupper(str[i]);
		else str[i] = tolower(str[i]);
	}
	cout << str;
	return 0;
}
