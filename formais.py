import copy
import random
from input import *


def printaVariaveis(variaveis):
    for variavel in variaveis:
        print(variavel,end=':\n')
        for sublista in variavel.getVarsTerms():
            for elemento in sublista:
                print(elemento, end=' ')
            print()
        print('')

def looping(variable):
     #Faz tudo igual a firstLooping, exceto a parte do firstSymbol
    if(variable.getClass() == "Terminal"):
        print("---" + variable.getValue() + "---")
    if (variable.getClass() == "Variable"):
        terms = variable.getRandomThing()
        for term in terms:
            looping(term)

def firstLooping(firstSymbol, variables):
    # Vai procurar o SimboloInicial em todas as variaveis e utilizar ela
    # para começar a criar a gramatica
    #a = variables[5]    bes = a.getVarsTerms()    cas = bes[0]    np = cas[0]    print(a, '\n', bes,' \n',cas,'\n',np)    print(np.getValue(),'    >>',np.getVarsTerms())
    #input()
    variable = getVar_fromList(firstSymbol,variables)
    if(variable.getClass() == "Terminal"): # Se for uma loucura a gramatica começar com um terminal, já printa ele
        print("---" + variable.getValue() + "---")

    elif (variable.getClass() == "Variable"):    # Se for uma Variavel, vai pegar um elemento randomico do seu lado esquerdo
        a = (variable.getVarsTerms())[0]
        terms = variable.getRandomThing()   # E executar do mesmo jeito esse termo
        for term in terms:
            looping(term)


if __name__ == '__main__':
    variaveis, terminais, startingVar = readInput("sample.txt")

    firstLooping(startingVar, variaveis)
