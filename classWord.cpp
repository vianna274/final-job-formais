#include "classHash.h"
#include <algorithm>
#include <stdlib.h>

Word::Word(std::string str, int ocurrences, float value, std::vector<int> linha){
        this->palavra = str;
        this->ocorrencias = ocurrences;
        this->valor = value;
        this->linhas.insert(linhas.end(),linha.begin(),linha.end());
}

///Getters & Setters
int Word::getOcorrencias(){
    return this->ocorrencias;
}

float Word::getValor(){
    return this->valor;
}

std::vector<int> Word::getLinhas(){
    return this->linhas;
}

std::string Word::getString(){
    return this->palavra;
}

///Methods
void Word::updateWord(float value, std::vector<int> linha){ ///Modifica os atributos da Word com os parametros recebidos
    this->valor = ((this->ocorrencias * this->valor) + value) / (this->ocorrencias + 1 );
    this->ocorrencias += 1;
    bool problem = false;
    for (int i = 0; i < (int)linha.size(); i++)
    {
        if (!(!(std::find(this->linhas.begin(), this->linhas.end(), linha[i]) != this->linhas.end()))){
            problem = true;
        }
    }
    if (!problem){
        this->linhas.insert(linhas.end(),linha.begin(),linha.end());
    }
}

bool Word::sameString(std::string str){///Retorna se a string passada equivale à palavra do Objeto Word

    if( this->palavra.compare(str) == 0){

        return true;
    }

    return false;
}

bool Word::isRadixWord(std::string radical){///Retorna se a string passada é radical da palavra do Objeto Word

    if (radical.size() > this->palavra.size()){

        return false;
    }

    for(int i = 0; i < ((int) (radical.size())) ; i++){

        if( radical[i] != this->palavra[i] ){

            return false;
        }

    }

    return true;
}
