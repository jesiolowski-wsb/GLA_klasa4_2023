// ekodom.cpp : Ten plik zawiera funkcję „main”. W nim rozpoczyna się i kończy wykonywanie programu.
//
#include <iostream>
#include <fstream>
using namespace std;

ifstream plik("ekodom.txt");

int main()
{
    string data;
    int retencja;
    string dataStart, dataEnd;
    string dSmax, dEmax; //dataStartmax i dataEndmax
    int bo = 0;
    int bomax = 0;
    for (int i = 0; i < 366; i++)
    {
        if (i > 0)
        {
            plik >> data >> retencja;
            //cout << data << "\t" << retencja << endl;
            if (retencja == 0)
            {
                if (bo == 0) dataStart = data;
                bo++;
                dataEnd = data;
            }
            else
            {
                if (bo > bomax)
                {
                    bomax = bo;
                    dSmax = dataStart;
                    dEmax = dataEnd;
                    bo = 0;
                }
                else bo = 0;
            }
        }
        else plik >> data >> data;
    }
    cout << bomax << "\t" << dSmax << "\t" << dEmax << endl;
}
