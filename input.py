import re
from variableClass import *
from terminalClass import *

def isTerminal(palavra, lista):
    retorno = False
    for i in lista:
        if i.getValue() ==  palavra:
            retorno = True
    return retorno

def getVar_fromList(value, lista):
    for x in lista:
        if x.getValue() == value:
            return x

def readInput():
    try: #Se testa abrir o arquivo sample.txt
        arquivo = open('sample.txt','r')
        palavras = []
        variaveis = []
        terminais = []  #Declaração de todas as variaveis a serem utilizadas
        varsTerms = []
        new_phrase = []
        case = 0
        startingWord = None
        flag = 0

        for line in arquivo: # A primeira linha contendo trash se ignora usando case 0 para quando ainda não se está lendo linhas corretas
            if case == 0:
                case += 1

            elif '[ ' and ' ]' in line: #Se tiver palavras válidas na linha ( dentro de [ ] )
                del new_phrase[:]
                new_phrase = re.findall(r'\[ ([^]]*)\ ]', line) #salva a ou as palavras da linha na lista de novas palavras

                if case == 1:
                    terminais.append( Terminal( new_phrase[0],None,None ) )

                elif case == 2:
                    if case == 2:
                        new_Variavel = Variable(new_phrase[0],None )
                        variaveis.append( new_Variavel )

                elif case == 4:
                    variavelAtual = getVar_fromList(new_phrase[0],variaveis) #Pega o objeto referente à variavel da esquerda da regra na list de variaveis
                    for elemento in new_phrase[1:] :
                        if not isTerminal(elemento,terminais):#O resto de variaveis ou terminais da regra serão adicionadas à varsTerms da variavel da esquerda
                            varGeradora = getVar_fromList(elemento,variaveis)
                            varsTerms.append(varGeradora)  #Se é uma variavel, se adiciona o objeto referente a ele à varsTerms da varaivel à esquerda

                        else: #Se nao estiver na lista de variaveis, é um terminal que vai para a lista varsTerms da variavel à esquerda
                            elemento = getVar_fromList(elemento,terminais)
                            varsTerms.append(elemento)

                    variavelAtual.appendTerm([]) #Cada termo do lado direito da regra será adicionado na nova lista de regras da var da esquerda
                    tam = len(variavelAtual.getVarsTerms())
                    for x in varsTerms:
                        variavelAtual.getVarsTerms()[tam-1].append(x)
                    del varsTerms[:]

            elif case == 1: #Depois de acabar de ler todos os terminais seta que case é 2, ou seja, proximas palavras a lerem serao variaveis
                case +=1

            elif case == 2: #Depois de acabar de ler todos as variaveis seta que case é 3, ou seja, proxima palavra a ser lida sera variavel inicial
                case +=1

            elif case == 3: #Depois de acabar de ler a variavel de inicio seta que case é 4, ou seja, proximas palavras a serem lida serao regras
                startingWord = new_phrase[0]
                case +=1

        return variaveis, terminais, startingWord

    except IOError: #Se nao conseguiu se abrir o arquivo
        print ('Could not open file! Please be sure sample.txt is in the same folder')
        exit()
