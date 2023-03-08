#include <iostream>
#include <string>

using namespace std;

int main(void)
{
	string str;
	double grade;
	
	cin >> str;

	if (str[0] == 'A')
	{
		grade = 4.0;
		if (str[1] == '+') grade = grade + 0.3;
		else if (str[1] == '-') grade = grade - 0.3;
	}
	else if (str[0] == 'B')
	{
		grade = 3.0;
		if (str[1] == '+') grade = grade + 0.3;
		else if (str[1] == '-') grade = grade - 0.3;
	}
	else if (str[0] == 'C')
	{
		grade = 2.0;
		if (str[1] == '+') grade = grade + 0.3;
		else if (str[1] == '-') grade = grade - 0.3;
	}
	else if (str[0] == 'D')
	{
		grade = 1.0;
		if (str[1] == '+') grade = grade + 0.3;
		else if (str[1] == '-') grade = grade - 0.3;
	}
	else grade = 0;

	cout.precision(1);
	cout << fixed << grade;


}
