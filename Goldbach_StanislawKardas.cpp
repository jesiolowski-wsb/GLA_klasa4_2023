#include <iostream>
#include <fstream>
#include <string>
using namespace std;

ifstream plik("liczby.txt");

bool czyP(int a) //czy pierwsza
{
	for (int i = 2; i < sqrt(a)+1; i++)
	{
		if (a % i == 0) return false;
	}
	return true;
}

int kP(int a) // kombinacje [liczby] pierwszej
{
	int licz = 0;
	for (int i = 4; i < a/2; i++)
	{
		if (czyP(i) && czyP(a - i)) licz++;
	}
	return licz;
}

string dec2hex(int a) //TODO: odwrócić!!!!
{
	string hex;
	int r;
	while (a > 0)
	{
		r = a % 16;
		if (r < 10) hex.push_back(char(r + 48));
		else  hex.push_back(char(r + 55));
		a /= 16;
	}
	return hex;
}

int main()
{
	int liczP = 0;
	int n;
	int kmax = 0;
	int nkmax;
	int k;
	int kmin = 2147483647;
	int nkmin;
	for (int i = 0; i < 100; i++)
	{
		plik >> n;
		//cout << n << "\t" << dec2hex(n) << endl;
		if (czyP(n - 1)) liczP++;
		k = kP(n);
		if (k > kmax)
		{
			kmax = k;
			nkmax = n;
		}
		if (k < kmin)
		{
			kmin = k;
			nkmin = n;
		}
	}
	cout << liczP << endl;
	cout << kmax << "\t" << nkmax << "\t" << kmin << "\t" << nkmin << endl;
}
