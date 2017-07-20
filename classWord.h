#ifndef CLASSWORD_H_INCLUDED
#define CLASSWORD_H_INCLUDED
#include "imports.h"

class Word{
    private:
        float valor;
        int ocorrencias;
        std::string palavra;
        std::vector<int> linhas;


    public:
        Word(std::string str, int ocurrences, float value, std::vector<int> linha);
        int getOcorrencias(); ///Getter
        std::vector<int> getLinhas();///Getter
        float getValor();///Getter
        std::string getString();///Getter
        void updateWord(float value, std::vector<int> linha); ///Atualiza os atributos de uma Word
        bool sameString(std::string palavra); ///Boolean que faz um strcmp
        bool isRadixWord(std::string radical); ///Boolean que testa se radical é subtstring inicial de string palavra
};


#endif // CLASSWORD_H_INCLUDED
