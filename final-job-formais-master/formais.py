# -*- coding: utf-8 -*-
import copy
import random
import web
from input import *

# a url /generate/ espera um parametro e eh tratada na classe gen
# a url files n espera nada e eh tratada na classe files
urls = ('/generate/(.*)', 'gen', '/files', 'files')
phrase = ""

def printaVariaveis(variaveis):
    for variavel in variaveis:
        print(variavel)
        for sublista in variavel.getVarsTerms():
            for elemento in sublista:
                print(elemento)
            print()
        print('')

def looping(variable):
    # cagada do python pra poder usar variavel global
    global phrase
     #Faz tudo igual a firstLooping, exceto a parte do firstSymbol
    if(variable.getClass() == "Terminal"):
        # vai concatenando na 'phrase' cada vez que chega num terminal
        phrase = phrase + variable.getValue() + " "
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
        phrase += variable.getValue() + " "

    elif (variable.getClass() == "Variable"):    # Se for uma Variavel, vai pegar um elemento randomico do seu lado esquerdo
        a = (variable.getVarsTerms())[0]
        terms = variable.getRandomThing()   # E executar do mesmo jeito esse termo
        for term in terms:
            looping(term)

def filesJSON(files):
    # a maior gambiarra da historia
    # retorna um JSON com todos os arquivos da lista de arquivos
    # nao vai ser usado na versao final do gerador de frases motiv.
    # esse vai usar so o sample que a lize e o rhoden vao fazer
    json = '{\"files\":['
    for i in range(0, len(files)-1):
        json = json + '\"' + str(files[i]) + '\",'
    json = json + '\"' + files[len(files)-1] + '\"]}'
    return json

class gen:
    def GET(self, pos):
        try:
            global phrase
            # reseta a phrase
            phrase = ""
            # eu recebo uma posicao na url, então pego como input
            # o arquivo que ta na posicao recebida
            # na versao final, vamos usar só um arquivo, entao vai simplificar
            files = ['sample.txt', 'sample1.txt', 'sample2.txt']
            variaveis, terminais, startingVar = readInput(files[int(pos)])
            # o looping vai preencher a phrase
            firstLooping(startingVar, variaveis)
            # aqui eu retorno ela
            return phrase
        except Exception as exp:
            # caso de qualquer merda, eu retorno escrita a merda que deu
            return str(exp)

class files:
    def GET(self):
        try:
            # retorna o JSON da lista de arquivos passada
            return str(filesJSON(['sample.txt', 'sample1.txt', 'sample2.txt']))
        except Exception as exp:
            return str(exp)
                


if __name__ == '__main__':
    # crio a aplicacao web passando as URLS dos meus serviços e rodo ela
    app = web.application(urls, globals())
    app.run()
    
