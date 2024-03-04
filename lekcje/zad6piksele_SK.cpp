// zad6_piksele.cpp : Ten plik zawiera funkcję „main”. W nim rozpoczyna się i kończy wykonywanie programu.
//

#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

ifstream plik1("przyklad.txt");
ifstream plik("dane.txt");

ofstream wynik("wyniki6.txt");

bool czy_sym(vector<int> w)
{
	for (int i = 0; i < w.size() / 2; i++)
	{
		if (w[i] != w[319 - i]) return false;
	}
	return true;
}

int main()
{
	vector<int> w(320); //wiersz
	vector<vector<int>> k(200); //kolumna
	int jmax = 0, jmin = 255; //najjaśniejszy i najciemniejszy pxl
	int dell = 0; //ile linijek do kasacji (zad 2) - linijki niepalindromiczne
	for (int i = 0; i < 200; i++) //iterowanie po wierszach
	{
		for (int j = 0; j < 320; j++) //iterowanie wewnątrz wierszy
		{
			plik >> w[j];
			//cout << w[j] << " ";
			//min/max:
			if (w[j] > jmax) jmax = w[j];
			if (w[j] < jmin) jmin = w[j];
		}
		//czy delete:
		if (!czy_sym(w)) dell++;
		//cout << endl;
		//w >> k
		k[i] = w;
	}
	//kontrastujace:
	int kntrs = 0;
	for (int i = 0; i < 200; i++)
	{
		for (int j = 0; j < 320; j++)
		{
			if (i > 0 && abs(k[i][j] - k[i - 1][j]) > 128) kntrs++;
			else if (j > 0 && abs(k[i][j] - k[i][j - 1]) > 128) kntrs++;
			else if (i < 199 && abs(k[i][j] - k[i + 1][j]) > 128) kntrs++;
			else if (j < 319 && abs(k[i][j] - k[i][j + 1]) > 128) kntrs++;
		}
	}
	cout << "1. Najjasniejszy pixel ma jasnosc " << jmax << " a najciemniejszy " << jmin << endl << "2. " << dell << endl << "3. " << kntrs << endl;
}

// Uruchomienie programu: Ctrl + F5 lub menu Debugowanie > Uruchom bez debugowania
// Debugowanie programu: F5 lub menu Debugowanie > Rozpocznij debugowanie

// Porady dotyczące rozpoczynania pracy:
//   1. Użyj okna Eksploratora rozwiązań, aby dodać pliki i zarządzać nimi
//   2. Użyj okna programu Team Explorer, aby nawiązać połączenie z kontrolą źródła
//   3. Użyj okna Dane wyjściowe, aby sprawdzić dane wyjściowe kompilacji i inne komunikaty
//   4. Użyj okna Lista błędów, aby zobaczyć błędy
//   5. Wybierz pozycję Projekt > Dodaj nowy element, aby utworzyć nowe pliki kodu, lub wybierz pozycję Projekt > Dodaj istniejący element, aby dodać istniejące pliku kodu do projektu
//   6. Aby w przyszłości ponownie otworzyć ten projekt, przejdź do pozycji Plik > Otwórz > Projekt i wybierz plik sln
