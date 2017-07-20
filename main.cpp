#include "tools.h"
#include <algorithm>
#include <string>
#include <conio.h>
#include <fstream>
using namespace std;


int main()
{
    /// Cria as variaveis utilizadas
    vector<string>  fileContent, palavrasRadicais,terminais,lineAux;
    vector<Word> valuesWords,ocurrencesWords;
    string line, phrase,palavra, radical,nomeSaida,nomeTSV;
    ifstream myfile;
    ofstream saidaCSV;
    bool firstTsv = false,sortedValues = false,sortedFreq = false;
    int  opt, k;
    HashTable tabela(2);
    Trie arvore;
    readVocabulary(&tabela,&arvore,fileContent);

    showMenu();
    cin >> opt;
    while(opt)
    {
        switch(opt)
        {
        case 1:                         ///Se le uma string que posteriormente é quebrada em varias strings, cada uma sendo avaliada e depois fazendo-se a média entre todas para retornar a nota
            cout << "Digite sua frase: ";
            cin.clear();
            fflush(stdin);
            getline(cin, phrase);
            cout << endl;
            std::transform(phrase.begin(), phrase.end(), phrase.begin(), ::tolower);
            classify(splitStr(phrase), &tabela,1);
            phrase.clear();
            cout <<endl <<endl<< "Press any key to Continue... ";
            getch();
            break;

        case 2:
        case 3:                          /// Vai dar quicksort uma unica vez e depois so se acessa os k primeiros ou k ultimos elementos
            cout  <<"Digite o K: ";
            cin >> k;
            cout << endl;
            if(!sortedValues)
            {
                if(!sortedFreq)
                {
                    valuesWords = tabela.fillVector();
                    ocurrencesWords = valuesWords;
                }
                quickSort(valuesWords,0,(int)valuesWords.size() - 1,1);
                sortedValues = true;
            }

            if (opt == 2)
            {
                cout<<k << " palavras com maior valor:"<<endl;
                for(int i =1 ; i <= k ; i++)
                    cout << valuesWords[(int) valuesWords.size()- i].getString()<<"\t\t" <<valuesWords[(int) valuesWords.size()- i].getValor() << endl;
            }

            else
            {
                cout<<k << " palavras com menor valor:"<<endl;
                for(int i = 0; i < k; i++)
                    cout << valuesWords[i].getString()<<"\t\t" <<valuesWords[i].getValor() << endl;
            }
            cout <<endl <<endl<< "Press any key to Continue... ";
            getch();
            break;

        case 4:                                                 /// Da quicksort uma unica vez e pega os k mais frequentes
            cout  <<"Digite o K: ";
            cin >> k;
            cout << endl <<k << " palavras mais frequentes:"<<endl;
            if(!sortedFreq)
            {
                if(!sortedValues)
                {
                    valuesWords = tabela.fillVector();
                    ocurrencesWords = valuesWords;
                }
                quickSort(ocurrencesWords,0,(int)ocurrencesWords.size() - 1,0);
                sortedFreq = true;
            }
            for(int i =1 ; i <= k ; i++)
                cout << ocurrencesWords[(int) ocurrencesWords.size()- i].getString()<< "\t\t" << ocurrencesWords[(int) ocurrencesWords.size()- i].getOcorrencias() << endl;
            cout <<endl <<endl<< "Press any key to Continue... ";
            getch();
            break;

        case 5:                                                 /// Recebe uma palavra é transformada em lowercase e é buscado seus comentarios
            cout << endl << "Digite a palavra: ";
            cin >> palavra;
            cout  << "Digite a polaridade, ou digite 5 para ignorar: ";
            cin >> k;
            if(k < 0 || k > 5){
                cout << "Voce eh burro analfabeto, vai se ignorar\n";
            }
            cout << endl<< "Nota e comentarios com a palavra " << palavra << " :" <<endl;
            std::transform(palavra.begin(), palavra.end(), palavra.begin(), ::tolower);
            searchComments(palavra, &tabela, k, fileContent);
            palavra.clear();
            cout <<endl <<endl<< "Press any key to Continue... ";
            getch();
            break;

        case 6:                                                 /// Recebe o radical e procura na Trie todas as palavras que tem esse radical
            cout <<"Digite o radical pelo qual quer procurar palavras :  ";
            cin >> radical;
            std::transform(radical.begin(), radical.end(), radical.begin(), ::tolower);
            cout <<endl <<"Palavras com radical " <<radical << " :"<<endl<< endl;
            terminais = arvore.radixWords(radical);
            for(int i = 0; i < (int)terminais.size(); i++)
            {
                cout << terminais[i]<<endl;
            }
            radical.clear();
            palavrasRadicais.clear();
            terminais.clear();
            cout <<endl <<endl<< "Press any key to Continue... ";
            getch();
            break;

        case 7:                                                     /// Le o arquivo TSV e da uma nota para cada frase e escreve em um csv
            cout << "Digite o nome do arquivo de entrada TSV com a extensao .tsv no final" <<endl;
            cin >>nomeTSV;
            myfile.open(nomeTSV.c_str());
            if ( myfile.is_open())
            {
                cout << "Digite o nome de arquivo de saida com o .csv no final" <<endl;
                cin >>nomeSaida;
                saidaCSV.open(nomeSaida.c_str());
                firstTsv = true;
                while(std::getline(myfile, line))       // '\n' is the default delimiter
                {
                    lineAux = splitStr(line);
                    if(!firstTsv)
                    {
                        saidaCSV << lineAux[0] << "," << classify(lineAux, &tabela,0) <<"\n";
                    }
                    else
                    {
                        firstTsv = false;
                        saidaCSV << "PhraseId,Sentiment" << endl;
                    }
                    lineAux.clear();
                }
                cout << "\nO arquivo " << nomeSaida<< " foi gerado com sucesso!" << endl;
            }
            else
                cout << "Arquivo inexistente, nao foi gerada nenhum output..." << endl;

            nomeSaida.clear();
            nomeTSV.clear();
            line.clear();
            myfile.close();
            saidaCSV.close();
            cout <<endl <<endl<< "Press any key to Continue... ";
            getch();
            break;

        case 8:
            system("cls");
            break;

        default:
            break;
        }
        cout << endl;
        showMenu();
        cin >> opt;
    }
    cout <<endl<< "Saindo do programa..." << endl;
    return EXIT_SUCCESS;
}
