#include <iostream>
#include <ctime>
#include <string>

using namespace std;

int main()
{
	time_t timer = time(NULL);
	struct tm* t = localtime(&timer);

	int year = t->tm_year + 1900;

	string month;
	string day;

	if (t->tm_mon + 1 < 10) month = "0" + to_string(t->tm_mon + 1);
	else month = t->tm_mon + 1;

	if (t->tm_mday < 10) day = "0" + to_string(t->tm_mday);
	else day = t->tm_mday;

	cout << year << "-" << month << "-" << day << "\n";
}
