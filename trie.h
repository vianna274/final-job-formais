#ifndef TRIE_H_INCLUDED
#define TRIE_H_INCLUDED


#include "classHash.h"

class Trie{

//private:
public:
    std::vector<Trie*> filhos;
    std::string prefixo;
    bool ehPalavra;


public:
    Trie();
    void insertWord(std::string str);///Insere uma palavra na Trie
    void recursionInsert(Trie** nodo,std::string str, int cont);///Vai descendo na trie, criando nodos se preciso, até chegar no nodo equivalente ou que formaria à palavra que se inseriu
    Trie* getRadixNode(Trie * nodo,std::string str, int cont,bool *flag);///Se retorna o nodo contendo o radical passado, portanto todos os filhos terão todas as palavras com radical passado
    std::vector<std::string> radixWords(std::string str); ///Retorna vector das strings que contem o radical passado
    void recursionSearch(Trie* nodo,std::string str,std::vector<std::string> &palavras);///Para cada nodo, testa se qualquer um dos filhos existem e possuirão strings com o radical
    ~Trie();
};

#endif // TRIE_H_INCLUDED
