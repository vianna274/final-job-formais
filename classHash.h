#ifndef CLASSHASH_H_INCLUDED
#define CLASSHASH_H_INCLUDED
#include "classWord.h"

class HashTable{
    private:
        typedef std::vector<Word*> wordVector;
        int tamanho;
        int ocupados;
        std::vector<Word*> myWords;


    private:
        int valorString(std::string str); ///Dada uma sequencia de caracteres (string) retorna um valor numerico associado a esse conjunto E ordem
        int chaveDivisao(int chave, int tamTabela); /// Metodo de hash
        int sondagemLinear(int pos,int i, int tamTabela); /// Metodo de tratamento de colisao
        wordVector::iterator getWord(std::string palavra,int position); ///Retorna um iterados de uma palavra Word na tabela Hash (auxiliar)
        void updateWord(std::string palavra,int position,float value,int ocurrences, std::vector<int> linha); ///Atualiza uma palavra, tanto criando como so atualizando
        Word getPosition(int position); ///Retorna a palavra na posicao passada
        void resizeTableInfos(); ///Metodo usado durante resize da hashTable

    public:
        HashTable(int Tam);
        int getTam();   /// Retorna tamanho
        int getOcupados(); /// Retorna o num de items ou quao ocupada esta a tabea
        int setItens(int itens);/// Seta o numero de items
        void insertWord(std::string nome,float value, int linha);   /// Insere uma Word na hash E se precisar da resize na tabela
        Word * getWordObject(std::string palavra);    /// Dado uma string retorna o objeto Word da tabela
        float valueWord(std::string palavra);   /// Dado uma palavra retorna sua pontuacao
        std::vector<Word*> getItems();  /// Retorna o vector da tabela hash
        void showNames();   /// Mostra tudo da hashtable
        std::vector<std::string> radixStrings(std::string radical); ///Retorna todas as strings com o radical passado
        std::vector<Word> fillVector(); /// Preenche o vector com todos os elementos da tabela hash
        ~HashTable(void);
};

#endif // CLASSHASH_H_INCLUDED
