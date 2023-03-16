#include <iostream>
#include <set>

using namespace std;

int main(void)
{
	int n, in;
	set<int>* arr = new set<int>;

	cin >> n;

	for (int i = 0; i < n; i++)
	{
		cin >> in;
		arr->insert(in);
	}

	for (int i : *arr) cout << i << "\n";

}
