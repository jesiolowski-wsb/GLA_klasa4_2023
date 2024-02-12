// spr120224_regex.cpp : Ten plik zawiera funkcję „main”. W nim rozpoczyna się i kończy wykonywanie programu.
//
#include <iostream>
#include <fstream>
#include <regex>
#include <vector>
using namespace std;

ifstream plik("numery.txt");
vector<bool> N(15);

int main()
{
	string numer;
	regex pattern("(.*)(0{3,}|1{3,}|2{3,}|3{3,}|4{3,}|5{3,}|6{3,}|7{3,}|8{3,}|9{3,})(.*)");
	//regex pattern("(\d)\1\1");
	for (int i = 0; i < 15; i++) N[i] = false;
	int licz = 0; //licz numery z min 3 takimi samymi znakami obok siebie
	int liczR = 0; //licz rodziny niepuste
	for (int i = 0; i < 1000; i++)
	{
		plik >> numer;
		if (regex_match(numer, pattern)) licz++;
		N[numer.length()-1] = true;
	}
	for (int i = 0; i < 15; i++) if (N[i]) liczR++;
	cout << licz << endl << liczR << endl;
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
