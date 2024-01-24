#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

ifstream plik("szachy.txt");

int rownowaga(vector<string> Q) // czy plansze są w równowadze (do zadania 2); kod sprzeczności = 64; kod prawdy = sumaryczna liczba bierek
{
	// białe bierki:
	int K = 0;
	int W = 0;
	int S = 0;
	int H = 0;
	int G = 0;
	int P = 0;
	// czarne bierki:
	int k = 0;
	int w = 0;
	int s = 0;
	int h = 0;
	int g = 0;
	int p = 0;
	// analiza planszy:
	for (int i = 0; i < 8; i++)
	{
		for (int j = 0; j < 8; j++)
		{
			// szukamy i katalogujemy figury:
			if (Q[i][j] == 'K') K++;
			if (Q[i][j] == 'W') W++;
			if (Q[i][j] == 'S') S++;
			if (Q[i][j] == 'H') H++;
			if (Q[i][j] == 'G') G++;
			if (Q[i][j] == 'P') P++;
			if (Q[i][j] == 'k') k++;
			if (Q[i][j] == 'w') w++;
			if (Q[i][j] == 's') s++;
			if (Q[i][j] == 'h') h++;
			if (Q[i][j] == 'g') g++;
			if (Q[i][j] == 'p') p++;
		}
	}
	// sprawdzamy równowagę:
	if (K != k) return 64;
	if (W != w) return 64;
	if (S != s) return 64;
	if (H != h) return 64;
	if (G != g) return 64;
	if (P != p) return 64;
	return K + W + S + H + G + P + k + w + s + h + g + p;
}

int main()
{
	vector<string> P(8); // Plansza
	// P[w][k] gdzie w to wiersz planszy a k - kolumna
	// do zadania 1:
	bool sprK; // sprawdzanie kolumny
	bool sprP; // sprawdzanie planszy
	int liczP = 0; // zliczanie plansz z pustymi kolumnami
	int liczK; // zliczanie pustych kolumn w planszy
	int maxK = 0; // przechowywanie największej liczby pustych kolumn w planszy
	// do zadania 2:
	int liczPR = 0; // zliczanie plansz w równowadze
	int slb; // sumaryczna liczba bierek - zwracana z funkcji rownowaga()
	int minslb = 64; // minimalna sumaryczna liczba bierek
	// do zadania 3:
	bool spr; // pomocnicza zmienna sprawdzająca czy znajdują się figury między wieżą a królem
	int bs = 0; // biała wieża szachuje czarnego króla
	int cs = 0; // czarna wieża szachuje białego króla
	for (int i = 0; i < 125; i++)
	{
		for (int i = 0; i < 8; i++) // czytanie z plik-u do P-lanszy
		{
			plik >> P[i];
		}
		// zadanie 1:
		sprP = false; // zakładamy, że plansza nie spełnia warunków
		liczK = 0; // zerujemy licznik pustych kolumn w planszy
		for (int i = 0; i < 8; i++)
		{
			sprK = true; // zakładamy, że kolumna spełnia warunki
			for (int j = 0; j < 8; j++)
			{
				if (P[j][i] != '.') sprK = false; // jeżeli kolumna nie spełnia warunków
			}
			if (sprK) // jeżeli kolumna spełnia warunki
			{
				sprP = true;
				liczK++;
			}
		}
		if (sprP) // jeżeli plansza spełnia warunki
		{
			liczP++;
			if (liczK > maxK) maxK = liczK; // aktualizacja największej wartości
		}
		// zadanie 2:
		slb = rownowaga(P); // przypisujemy zmiennej wynik funkcji dla danej planszy
		if (slb != 64) liczPR++; // sprawdzamy czy plansza jest w równowadze
		if (slb < minslb) minslb = slb; // aktualizacja najmniejszej wartości
		// zadanie 3:
        for (int i = 0; i < 8; i++)
        {
            for (int j = 0; j < 8; j++)
            {
                // czarna wieża białego króla:
                if (P[i][j] == 'K')
                {
                    // szukanie wieży po kolumnach:
                    for (int k = 0; k < 8; k++)
                    {
                        if (P[i][k] == 'w')
                        {
                            spr = true;
                            // sprawdzanie czy są figury między wieżą a królem:
                            if (k > j)
                            {
                                for (int n = j + 1; n < k; n++)
                                {
                                    if (P[i][n] != '.') spr = false;
                                }
                            }
                            if (j > k)
                            {
                                for (int n = k + 1; n < j; n++)
                                {
                                    if (P[i][n] != '.') spr = false;
                                }
                            }
                            // jeżeli nie ma figur (spr == true) to szach
                            if (spr == true) cs++;
                        }
                    }
                    // szukanie wieży po wierszach
                    for (int w = 0; w < 8; w++)
                    {
                        if (P[w][j] == 'w')
                        {
                            spr = true;
                            // sprawdzanie czy są figury między wieżą a królem:
                            if (w > i)
                            {
                                for (int n = i + 1; n < w; n++)
                                {
                                    if (P[n][j] != '.') spr = false;
                                }
                            }
                            if (i > w)
                            {
                                for (int n = w + 1; n < i; n++)
                                {
                                    if (P[n][j] != '.') spr = false;
                                }
                            }
                            // jeżeli nie ma figur (spr == true) to szach
                            if (spr == true) cs++;
                        }
                    }
                }
                // biała wieża czarnego króla:
                if (P[i][j] == 'k')
                {
                    // szukanie wieży po kolumnach:
                    for (int k = 0; k < 8; k++)
                    {
                        if (P[i][k] == 'W')
                        {
                            spr = true;
                            // sprawdzanie czy są figury między wieżą a królem:
                            if (k > j)
                            {
                                for (int n = j + 1; n < k; n++)
                                {
                                    if (P[i][n] != '.') spr = false;
                                }
                            }
                            if (j > k)
                            {
                                for (int n = k + 1; n < j; n++)
                                {
                                    if (P[i][n] != '.') spr = false;
                                }
                            }
                            // jeżeli nie ma figur (spr == true) to szach
                            if (spr == true) bs++;
                        }
                    }
                    // szukanie wieży po wierszach
                    for (int w = 0; w < 8; w++)
                    {
                        if (P[w][j] == 'W')
                        {
                            spr = true;
                            // sprawdzanie czy są figury między wieżą a królem:
                            if (w > i)
                            {
                                for (int n = i + 1; n < w; n++)
                                {
                                    if (P[n][j] != '.') spr = false;
                                }
                            }
                            if (i > w)
                            {
                                for (int n = w + 1; n < i; n++)
                                {
                                    if (P[n][j] != '.') spr = false;
                                }
                            }
                            // jeżeli nie ma figur (spr == true) to szach
                            if (spr == true) bs++;
                        }
                    }
                }
            }
        }
	}
	cout << "zadanie 1: \t" << liczP << "\t" << maxK << endl;
	cout << "zadanie 2: \t" << liczPR << "\t" << minslb << endl;
    cout << "zadanie 3: \t" << bs << "\t" << cs << endl;
}
