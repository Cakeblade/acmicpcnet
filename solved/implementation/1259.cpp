#include <iostream>
#include <string>

using namespace std;

int main(void)
{
	string str;

	cin >> str;
	while(str != "0")
	{
		bool flag = true;
		int beg = 0;
		int end = str.length() - 1;
		int mid = str.length() / 2;
		
		while (beg != mid)
		{
			if (str[beg] != str[end])
			{
				flag = false;
				break;
			}
			else
			{
				beg++;
				end--;
			}
		}
		
		if (flag) cout << "yes" << "\n";
		else cout << "no" << "\n";

		cin >> str;
	}
}
