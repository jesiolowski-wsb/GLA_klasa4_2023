// spr190224_regex.cpp : Ten plik zawiera funkcję „main”. W nim rozpoczyna się i kończy wykonywanie programu.
//

#include <iostream>
#include <regex>
#include <sstream>
#include <vector>
using namespace std;

int main()
{
	string tekst = "(...) Historia przegiegu tranzakcji sklepu X: anna_kowalska@wp.pl zakupił(a) produkt od marcin.lewandowski@gmail.org jakiś czas potem sprzedając go dalej dodając marżę w wysokości 25% tak że produkt wylądował u johnDoe@sample.net. Następnie historia traci klarowność - w bazie mamy informację jedynie o adresie unknown-person@o2.pl";
	regex pattern("[A-Za-z0-9._%+-]+@\\w+\\.[A-Za-z]{2,}");
	regex polska("[A-Za-z0-9._%+-]+@\\w+\\.pl");
	istringstream ss(tekst);
	string slowo;
	string email;
	int pl = 0; //adresy z polski - licz
	vector<string> PL;
	while (getline(ss, slowo, ' '))
	{
		//cout << slowo << endl;
		if (!slowo.empty() && (slowo.back() == '.' || slowo.back() == ',')) slowo.pop_back();
		if (regex_match(slowo, pattern))
		{
			cout << slowo << endl;
			if (regex_match(slowo, polska))
			{
				pl++;
				PL.push_back(slowo);
			}
		}
	}
	cout << "adresów z Polski:\t" << pl << endl;
	for (int i = 0; i < PL.size(); i++) cout << PL[i] << endl;
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
