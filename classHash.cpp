#include "classHash.h"
int ajuda;
HashTable::HashTable(int tam)
{
    tamanho = tam;
    ocupados = 0;
    for (int i = 0; i < tamanho; i++)
        myWords.push_back(NULL);
}

///Setters & Getters
int HashTable::getTam()
{
    return tamanho;
}

int HashTable::getOcupados()
{
    return ocupados;
}

std::vector<Word*> HashTable::getItems()
{
    return myWords;
}

int HashTable::setItens(int itens)
{
    if (itens <= tamanho)
    {
        ocupados = itens;
        return 1;
    }

    return 0;std::cout << "Desalocando Trie...\n" ;
}

void HashTable::resizeTableInfos()
{

    tamanho = tamanho * 2 + 1;
    ocupados = 0;
}

///Methods
int HashTable::valorString(std::string str) ///Retorna um valor associado a uma string (31 e 7 como valores primos arbitrarios, podendo ser qualquer outro primo)
{
    int i,valor = 7;
    int tam = str.size();
    for(i = 0; i < tam; i++)
    {
        valor = 31 * valor + (int) str[i];
    }
    return valor;
}

int HashTable::chaveDivisao(int chave, int tamTabela) ///Retorna um valor associado � chave passada
{
    return (chave & 0x7FFFFFFF) % tamTabela;
}

int HashTable::sondagemLinear(int pos,int i, int tamTabela)  ///Se h� colis�o, procura pelo elemento nas pr�ximas posi��es da Tabela Hash
{

    return ( ((pos + i) & 0x7FFFFFFF) % tamTabela );
}

HashTable::wordVector::iterator HashTable::getWord(std::string palavra,int position)  ///Retorna o Objeto Word correspondente � string passada
{

    int newPos;
    wordVector::iterator it = myWords.end();

    for(int i =0; i<getTam(); i++)
    {
        newPos = sondagemLinear(position,i,getTam());

        if(myWords[newPos] == NULL || myWords[newPos]->sameString(palavra) )
        {
            it = myWords.begin()+newPos;
            break;
        }

    }
    return it;
}

Word * HashTable::getWordObject(std::string palavra)
{
    int position = chaveDivisao(valorString(palavra),getTam());
    return *(getWord(palavra, position));
}

void HashTable::updateWord(std::string str,int position,float value,int ocurrences, std::vector<int> linha)  ///Atualiza o Objeto Word correspondente � string
{

    wordVector::iterator it = getWord(str,position);
    if( (*it) != NULL)
    {
        (*it)->updateWord(value, linha);
    }
    else
    {
        (*it) = new Word(str,ocurrences,value, linha);
        setItens(getOcupados() +1);
    }
}

void HashTable::insertWord(std::string nome,float value,int linha)  ///Atualizar� ou criar� um Objeto Word com a string e valor passados e dar resize na hash table se preciso
{
    std::vector<int> linhas;
    linhas.push_back(linha);

    int position = chaveDivisao(valorString(nome),getTam());
    updateWord(nome,position,value,1, linhas);

    if( (float)getOcupados() >= ((float) getTam() * 0.75) )
    {
        std::vector<Word*> oldWords = myWords;
        myWords.clear();
        for (int i = 0; i < getTam() * 2 + 1; i++)
        {
            myWords.push_back(NULL);

        }
        resizeTableInfos();

        for(int i = 0; i < (int)oldWords.size(); i++ ){
                if(oldWords[i]!=NULL)
                    updateWord(oldWords[i]->getString(),chaveDivisao(valorString(oldWords[i]->getString()),getTam()),oldWords[i]->getValor(),oldWords[i]->getOcorrencias(),oldWords[i]->getLinhas());
        }
        oldWords.clear();
    }
}

float HashTable::valueWord(std::string palavra)  ///Retorna o valor do Objeto Word correspondente � string passada
{
    wordVector::iterator it = getWord(palavra,chaveDivisao(valorString(palavra),getTam()));
    if (*it == NULL)
        return 2;
    else
    {
        float valor = (*it)->getValor();
        return valor;
    }
}

Word HashTable::getPosition(int position) ///Retorna Word na posicao passada da hash table
{
    return *(myWords[position]);

}

std::vector<std::string> HashTable::radixStrings(std::string radical)///Retorna vector com as strings contendo o radical
{
    std::vector<std::string> palavrasRadicais;
    for(int i = 0; i < getTam(); i ++)
    {
        if(myWords[i]!=NULL)
        {
            if(myWords[i]->isRadixWord(radical))
            {
                palavrasRadicais.push_back(myWords[i]->getString());
            }
        }

    }

    return palavrasRadicais;
}

std::vector<Word> HashTable::fillVector() ///Preenche um vector com todas as Word da tabela Hash
{
    std::vector<Word> valores;
    int copiados = 0;
    for(int i = 0; i < getTam(); i++)
    {

        if (myWords[i]!=NULL)
        {
            valores.push_back( *(myWords[i]) );
            copiados++;

            if (copiados == getOcupados())
            {
                break;
            }
        }

    }
    return valores;
}

void HashTable::showNames()  ///M�todo que mostra toda a tabela Hash
{
    for(int i = 0; i < getTam(); i++)
    {
        if(myWords[i] != NULL)
            std::cout << "palavra  = " << myWords[i]->getString() <<"  valor = " << myWords[i]->getValor() <<"  ocorrencias = " << myWords[i]->getOcorrencias() << std::endl;
        else
            std::cout << "NULL"<< std::endl;
    }
    std::cout << std::endl;
}

HashTable::~HashTable(void)
{
    std::cout << "Vector ... deleting" << std::endl<< std::endl;
    for (int i = 0; i < tamanho; i++)
    {
        if (myWords[i] != NULL)
            delete myWords[i];
    }
    std::cout << std::endl<< "Vector ... deleted" << std::endl;
    myWords.clear();
}
