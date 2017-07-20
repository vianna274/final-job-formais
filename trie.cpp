#include "trie.h"

Trie::Trie()
{
    for (int i =0; i <26; i++ )
        filhos.push_back(NULL);
}



void Trie::insertWord(std::string str)///Do nodo pai, que é coringa, se vai para o filho equivalente à primeira letra da string
{
    int cont = 1,index;
    index = (int) str[0] - (int) 'a';
    recursionInsert(&(filhos[index]),str,cont);
}

void Trie::recursionInsert(Trie** nodo,std::string str, int cont)///Vai testando se chegou no nodo que deveria ser onde estaria inserida a palavra.Senao vai criando e descendo pelo filho equivalente
///ao char da posicao atual da string
{
    if(*nodo == NULL)
    {
        (*nodo) = new Trie();
        (*nodo)->ehPalavra = false;
        (*nodo)->prefixo.append(str,0,cont);
    }

    if( (*nodo)->prefixo.compare(str)!= 0)
        recursionInsert(&((*nodo)->filhos[ ((int) str[cont] - (int) 'a') ]),str,cont+1 );
    else
        (*nodo)->ehPalavra = true;
}

Trie * Trie::getRadixNode(Trie * nodo,std::string str, int cont,bool *flag)///A partir de um radical, desce até o nodo que contem todo esse radical para deixar "pronto" depois só pegar todos os filhos desse nodo
{
    if(nodo == NULL)
        *flag = *flag | false;
    else
    {
        if((int) str.size() == cont)
        {
            *flag = *flag | true;
            return nodo;
        }
        return getRadixNode(nodo->filhos[ (int) str[cont] - (int) 'a' ],str,cont+1,flag);
    }
}


std::vector<std::string> Trie::radixWords(std::string str)///Se consegue achar um nodo a partir de um radical, se faz recursao para pegar todas as palavras abaixo/em nodos filhos desse nodo
{
    std::vector<std::string> palavras;

    bool flag = false;
    Trie * nodoInicio = getRadixNode(filhos[ (int)str[0] - (int) 'a'  ],str,1,&flag);

    if(flag)
        recursionSearch(nodoInicio,str,palavras);

    return palavras;
}

void Trie::recursionSearch(Trie* nodo,std::string str,std::vector<std::string> &palavras)///Se vai descendo na Trie pra todos os n filhos de cada nodo e adicionando ao vector se foi achado uma substring que eh palavra
{
    if(nodo !=NULL)
    {
        if(nodo->ehPalavra)
            palavras.push_back(nodo->prefixo);
        for(int i = 0; i < 26; i++)
        {
            if(nodo->filhos[i]!=NULL)
            {
                recursionSearch(nodo->filhos[i],str,palavras);
            }
        }
    }
}

Trie::~Trie()
{
    for (int i = 0; i < 26; i++)
        delete filhos[i];
}
