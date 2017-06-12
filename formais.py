import re
import copy
from random import randint

class Variable():
    def __init__(self, valor, termos):
        self.setValue(valor)
        self.varsTerms = []

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def appendTerm(self,termos):
        self.varsTerms.append(termos)

    def expendTerm(self,termos):
        self.varsTerms.extend(termos)

    def getVarsTerms(self):
        return self.varsTerms

    def getRandomThing(self): # Retorna um elemento aleatório do "varTerms"
        lenghtTerms = len(self.varsTerms)
        randomTerm = self.varsTerms[randint(0,lenghtTerms-1)]
        return randomTerm

    def getClass(self):
        return "Variable"

    def __str__(self):
        return "Variable " + str(self.value)

class Terminal():
    def __init__(self, value, genre, number):
        self.setValue(value)
        self.setGenre(genre)
        self.setNumber(number)

    def __str__(self):
        return "Terminal " + str(self.value)

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def setGenre(self, genre):
        self.genre = genre

    def getGenre(self):
        return self.genre

    def setNumber(self, number):
        self.number = number

    def getNumber(self):
        return self.number

    def getClass(self):
        return "Terminal"

def isTerminal(palavra, lista):
    retorno = False
    for i in lista:
        if i.getValue() ==  palavra:
            retorno = True
    return retorno

def printaVariaveis(variaveis):
    for variavel in variaveis:
        print(variavel,end=':\n')
        for sublista in variavel.getVarsTerms():
            for elemento in sublista:
                print(elemento, end=' ')
            print()
        print('')

#def firstLooping(firstSymbol, variables):
    # Vai procurar o SimboloInicial em todas as variaveis e utilizar ela
    # para começar a criar a gramatica
#    for variable in variables:
#        if variable.getValue() == firstSymbol:
            # Se for uma loucura a gramatica começar com um terminal, já printa ele
#            if(variable.getClass() == "Terminal"):
#                print(variable.getValue())
            # Se for uma Variavel, vai pegar um elemento randomico do seu lado esquerdo
            # E executar do mesmo jeito esse termo
#            if (variable.getClass() == "Variable"):
#                terms = variable.getRandomThing()
#                for term in terms:
#                    looping(term)

#def looping(variable):
    # Faz tudo igual a firstLooping, exceto a parte do firstSymbol
#    if(variable.getClass() == "Terminal"):
#        print(variable.getValue())
#    if (variable.getClass() == "Variable"):
#        terms = variable.getRandomThing()
#        for term in terms:
#            looping(term)



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

        for line in arquivo: # A primeira linha contendo trash se ignora usando case 0 para quando ainda não se está lendo linhas corretas
            if case == 0:
                case += 1

            elif '[ ' and ' ]' in line: #Se tiver palavras válidas na linha ( dentro de [ ] )
                del new_phrase[:]
                new_phrase = re.findall(r'\[ ([^]]*)\ ]', line) #salva a ou as palavras da linha na lista de novas palavras

                if case == 4:   #Se estiver lendo as regras, tem mais de 1 palavra na linha
                    del varsTerms[:]
                    for variavelAtual in variaveis: #Procura a variavel da esquerda da regra na lsita de variaveis
                            if variavelAtual.getValue() == new_phrase[0]:
                                    for elemento in new_phrase[1:] :  #Procura as variaveis da direita na lista de variaveis e adiciona elas na varsTerms
                                        if not isTerminal(elemento,terminais): #                                                    (lista de variveis)
                                            for varGeradora in variaveis:
                                                    if varGeradora.getValue() == elemento:
                                                        varsTerms.append(varGeradora)

                                        else: #Se nao estiver na lista de variaveis, é um terminal que vai para a lista varsTerms da variavel à esquerda
                                            varsTerms.append(elemento)
                                    variavelAtual.appendTerm(copy.deepcopy(varsTerms))

                else: #Senao é apenas 1 e só instancia objeto que ela é e adiciona à sua lista correspondente
                    if case == 1:
                        terminais.append( Terminal( new_phrase[0],None,None ) )
                    elif case == 2:
                        new_Variavel = Variable(new_phrase[0],None )
                        variaveis.append( new_Variavel )

            elif case == 1: #Depois de ler todos os terminais seta que case é 2, ou seja, proximas palavras a lerem serao variaveis
                case +=1

            elif case == 2: #Depois de ler todos as variaveis seta que case é 3, ou seja, proxima palavra a ser lida sera variavel inicial
                case +=1

            elif case == 3: #Depois de ler a variavel de inicio seta que case é 4, ou seja, proximas palavras a serem lida serao regras
                startingWord = new_phrase[0]
                case +=1

        return variaveis, terminais, startingWord

    except IOError: #Se nao conseguiu se abrir o arquivo
        print ('Could not open file! Please be sure sample.txt is in the same folder')


if __name__ == '__main__':
    variaveis, terminais, startingVar = readInput()
    printaVariaveis(variaveis)
