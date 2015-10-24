#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() 
{
	/* Enter your code here. Read input from STDIN. Print output to STDOUT */   
	using namespace std;

	vector<int> i;
	int x = 0;

	for(int y = 0; y < 4; y++)
	{
		cin >> x;
		i.push_back(x);
	}
	
	for(int y = 0; y < 4; y++)
	{
		cout << i[y] << endl;
	}
	
	return 0;
}
