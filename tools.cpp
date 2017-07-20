#include "tools.h"
#include <math.h>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <ctime>

using namespace std;


bool checkAlpha(string str)
{
    for(int i = 0; i < (int)str.size(); i++)
        if( !isalpha(str[i]))
            return false;
    return true;
}

void readVocabulary(HashTable * tabela, Trie * arvore,std::vector<std::string> &fileContent){ ///leitura e tratamento do input e passar para as ED

    ifstream myfile ("input.txt");
    string line, phrase,palavra,tempString;
    vector<string> lineWords,filtering = fillingFilter();
    int index=0;

    if (! myfile.is_open())
    {
        cout << "Unable to open file";
        exit(EXIT_FAILURE);
    }

    while ( getline (myfile,line) )
    {
        fileContent.push_back(line);
        lineWords = splitStr(line); /// Separa em um vector cada palavra da linha
        for(int i = 1; i < (int) lineWords.size() -1; i++)
        {
            tempString = lineWords[i];
            std::transform(tempString.begin(), tempString.end(), tempString.begin(), ::tolower); ///Bota o .txt em lower case
            if (!alreadyInsideString(filtering, tempString) && checkAlpha(tempString)) ///Elimina palavras stopword e palavras contendo não-somente caracteres letra
            {
                tabela->insertWord(tempString,(float) atof(lineWords[0].c_str()), index); /// Insere palavra por palavra na hash e na trie
                arvore->insertWord(tempString);
            }
        }
        index++;
    }

    myfile.close();
}



vector<string> splitStr(string str) ///Dado um string de entrada, retorna um vector com todas as palavras da string (string.split() implementado na mão)
{

    istringstream iss(str);
    vector<string> palavras;
    while (iss)
    {
        string word;
        iss >> word;
        palavras.push_back(word);
    }

    return palavras;
}

int classify(vector<string> words, HashTable * tabela, int printarResposta) ///Avaliar as palavras recebidas e retornas sua nota média
{
    Word * tempWord;
    float total=0,valor;
    int desconhecidas=0;
    if (!words.empty())
    {
        for(int i = 0; i < (int) words.size() -1; i++)
        {
            tempWord = tabela->getWordObject(words[i]);
            if (tempWord != NULL)
            {
                valor = tempWord->getValor();
                total += valor;
            }
            else
            {
                desconhecidas++;
            }
        }
        total = total/(words.size()-1-desconhecidas);
        if (desconhecidas == (int) words.size() - 1)
            total = 2;
        if (printarResposta)
        {
            std::cout << "O valor da frase e: " << total <<endl;
            if (total > 2)
                std::cout << "A frase e positiva" << endl;
            else if (total < 2)
                std::cout << "A frase e negativa" << endl;
            else
                std::cout << "A frase e neutra" << endl;
        }
    }
    else
    {
        if (printarResposta)
        {
            std::cout << "Voce digitou uma frase vazia!" << endl;
        }
    }
    total = round(total);
    return (int) total;
}

void searchComments(string entrada, HashTable * tabela, int pontuacao, vector<string> fileContent)///Procura por comments contendo a palavra passada e opcionalmente a pontuacao
{
    Word * palavra;
    palavra = tabela->getWordObject(entrada);
    if(palavra!=NULL){
    vector<int> linhas = palavra->getLinhas();
    vector<string> lineWords;
    int valor;
    for(std::vector<int>::iterator it = linhas.begin(); it != linhas.end(); ++it)
    {
        if (pontuacao < 5 && pontuacao >= 0)
        {
            lineWords = splitStr(fileContent[*it]);
            istringstream  (lineWords[0]) >> valor;
            if ((valor == pontuacao))
                cout << fileContent[*it] << endl;
        }
        else
            cout << fileContent[*it] << endl;
    }
}
}

void showMenu(){ ///Menu

    cout << endl;
    cout << "========= MENU ==========" << endl;
    cout << "1 - Classificar novo comentario" << endl;
    cout << "2 - Mostrar os K mais positivos" << endl;
    cout << "3 - Mostrar os K mais negativos" << endl;
    cout << "4 - Mostrar os K mais frequentes" << endl;
    cout << "5 - Buscar comentarios associados a uma palavra" << endl;
    cout << "6 - Buscar palavras por radical" << endl;
    cout << "7 - Teste a partir de um arquivo" << endl;
    cout << "8 - Limpar a tela" << endl;
    cout << "0 - Sair" << endl;
    cout << "==========================" << endl;
    cout << endl << "Digite sua opcao: ";


}

vector<string> fillingFilter()///Stopwords
{
    vector<string> temp;
    temp.push_back(",");
    temp.push_back(".");
    temp.push_back("a");
    temp.push_back("o");
    temp.push_back("the");
    temp.push_back("an");
    temp.push_back("and");
    temp.push_back("of");
    temp.push_back("to");
    temp.push_back("'s");
    temp.push_back("is");
    temp.push_back("that");
    temp.push_back("in");
    temp.push_back("it");
    temp.push_back("an");
    temp.push_back("as");
    temp.push_back("this");
    temp.push_back("for");
    temp.push_back("but");
    temp.push_back("its");
    temp.push_back("n't");
    temp.push_back("on");
    temp.push_back("...");
    temp.push_back("~");
    temp.push_back("`");///Getter
    temp.push_back("´");
    temp.push_back(";");
    temp.push_back("'");
    temp.push_back("``");
    return temp;
}

bool alreadyInsideString (vector<string> lista, string palavra) ///Metodo que diz se a palavra esta na lista de palavras
{
    for (int i = 0; i < (int) lista.size(); i++)
    {
        if(lista[i] == palavra)
            return true;
    }
    return false;
}
void quickSort(std::vector<Word> &arr, int left, int right, bool flag)///String sort para ordenar as palavras a partir de ser valor ou sua ocorrencia dependendo flag
{
    int i = left, j = right;
    float pivot;

    if (flag)
    {
        pivot = arr[(left + right) / 2].getValor();
    }
    else
    {
        pivot = (float) arr[(left + right) / 2].getOcorrencias();
    }

    /* partition */
    while (i <= j)
    {

        if (flag)
        {
            while (arr[i].getValor() < pivot)
                i++;
        }
        else
        {
            while ( (float)arr[i].getOcorrencias() < pivot)
                i++;
        }



        if(flag)
        {
            while (arr[j].getValor() > pivot)
                j--;
        }
        else
        {
            while ((float)arr[j].getOcorrencias() > pivot)
                j--;
        }
        if (i <= j)
        {
            std::swap(arr[i],arr[j]);
            i++;
            j--;
        }
    };

    /* recursion */
    if (left < j)
        quickSort(arr, left, j,flag);
    if (i < right)
        quickSort(arr, i, right,flag);
}
