#include <iostream>
#include <algorithm>

using namespace std;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n, m, in;
	
	cin >> n;
	int* arr = new int[n];

	for (int i = 0; i < n; i++) cin >> arr[i];

	sort(arr, arr + n);

	cin >> m;

	for (int i = 0; i < m; i++)
	{
		cin >> in;

		if (binary_search(arr, arr + n, in)) cout << 1 << "\n"; // 아니 std에 별게 다 있네 
		else cout << 0 << "\n";
		
	}

}
