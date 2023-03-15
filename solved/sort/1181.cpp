#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

bool compare(string a, string b)
{
	return a.size() < b.size();
}

int main(void)
{
	int n;
	string str;
	vector<string> words;

	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> str;
		if (find(words.begin(), words.end(), str) == words.end()) words.push_back(str);
	}

	stable_sort(words.begin(), words.end());
	stable_sort(words.begin(), words.end(), compare);

	for (unsigned long i = 0; i < words.size(); i++) 
	{
		cout << words[i] << "\n";
	}
}
