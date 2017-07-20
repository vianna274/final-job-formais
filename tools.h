#ifndef TOOLS_H_INCLUDED
#define TOOLS_H_INCLUDED

#include "trie.h"

bool checkAlpha(std::string str);///Boolean que checa se a string contem apenas letras
void readVocabulary(HashTable *tabela,Trie *arvore,std::vector<std::string>&fileContent); ///Leitor de arquivo de input e preenchimento a partir dela da hash e trie
std::vector<std::string> splitStr(std::string str); /// Divide uma string em um vector de strings
void searchComments(std::string palavra, HashTable * tabela, int pontuacao, std::vector<std::string> fileContent); /// Procura os comentários relacionados a uma palavra
int classify(std::vector<std::string> entrada, HashTable * tabela, int flag);   /// Retorna a pontuação da frase
void showMenu();    /// Mostra menu
std::vector<std::string> fillingFilter();   /// Preenche o vector de filtros
bool alreadyInsideString (std::vector<std::string> lista, std::string palavra); /// Verifica se uma string já está dentro de um vector de strings
void quickSort(std::vector<Word> &arr, int left, int right, bool printarResposta); /// QuickSort implementado para agilizar as buscar dos N pos, N neg e N freq
#endif // TOOLS_H_INCLUDED
