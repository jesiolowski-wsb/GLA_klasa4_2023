// zad1_analizatxtu.cpp : Ten plik zawiera funkcję „main”. W nim rozpoczyna się i kończy wykonywanie programu.
//
#include <iostream>
#include <fstream>
//#include <regex>
#include <vector>
using namespace std;

ifstream plik("tekst.txt");

string word(string s) // preparowanie słowa na małe litery od a do z
{
	for (int i = 0; i < s.length(); i++)
	{
		if (64 < int(s[i]) && int(s[i]) < 91) s[i] = char(int(s[i]) + 32); //podmianka wielkich liter na małe
		if (int(s[i]) < 97 || int(s[i]) > 122) s.erase(s.begin() + i); // usuwanie wszystkiego co nie jest literami
	}
	return s;
}

int czy_istnieje(string s, vector<string> U)
{
	for (int i = 0; i < U.size(); i++)
	{
		if (U[i] == s) return i;
	}
	return -1;
}

int main()
{
	string s;
	//regex pattern1("[,.'\"]");
	//regex pattern2("['\"]");
	int liczS = 0; // licznik słów
	vector<string> US; // unikalne słowa dump bin
	vector<int> WS; // występowanie słów (ile razy dane słowo)
	int indeks; // indeks wspólny dla US i WS
	while (plik.good())
	{
		s = "";
		plik >> s;
		//if (regex_match(s, pattern1)) s.pop_back();
		//if (regex_match(s, pattern2)) s.erase(0, 1);
		s = word(s);
		liczS++;
		indeks = czy_istnieje(s, US);
		if (indeks == -1)
		{
			US.push_back(s);
			WS.push_back(1);
		}
		else WS[indeks]++;
		//cout << s << endl;
	}
	//for (int i = 0; i < 128; i++) cout << i << "\t" << char(i) << endl;
	//for (int i = 0; i < US.size(); i++) cout << i << " " << US[i] << endl;
	int Wmax = 0; // najwięcej wystąpień
	int WImax = 0; // indeks najczęściej występującego wyrazu
	for (int i = 0; i < WS.size(); i++)
	{
		if (WS[i] > Wmax)
		{
			Wmax = WS[i];
			WImax = i;
		}
	}
	cout << "Odp. " << liczS - 1 << "\t" << US.size() - 1 << " " << US[WImax] << endl;
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
