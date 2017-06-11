#user.py
from random import randint

class GeneralClass():
    value = None
    varsTerms = []
    totalmenteVisitado = None
    estado = None

    # mainVar = variavels da esquerda
    # mainVar = variavel da esquerda
    # varsTerms = lista de tuplas [(V, "var"),("*", "ponto") (R,"var"), ("oi","term")]
    def __init__(self, value, varsTerms, estado):
        self.setValue(value)
        self.varsTerms = []
        self.setTotalmenteVisitado(False)
        self.setEstado(estado)

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def setVarsTerms(self,terms):
        self.varsTerms.append(terms)

    def getVarsTerms(self):
        return self.varsTerms

    def setTotalmenteVisitado(self,totalmenteVisitado):
        self.totalmenteVisitado = totalmenteVisitado

    def getTotalmenteVisitado(self):
        return self.totalmenteVisitado

    def setEstado(self,estado):
        self.estado = estado

    def getEstado(self):
        return self.estado

class Variable(GeneralClass):
    def __init__(self,value, varsTerms, estado):
        GeneralClass.__init__(self,value, varsTerms, estado)

    def __str__(self):
        return "Variable " + str(self.value)

    def getRandomThing(self):
        lenghtTerms = len(self.varsTerms)
        randomTerm = self.varsTerms[randint(0,lenghtTerms-1)]
        return randomTerm

    def getClass(self):
        return "Variable"

class Terminal():
    genre = None
    number = None
    value = None

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

def firstLooping(firstSymbol, variables):
    for variable in variables:
        if variable.getValue() == firstSymbol:
            if(variable.getClass() == "Terminal"):
                print(variable.getValue())
            if (variable.getClass() == "Variable"):
                terms = variable.getRandomThing()
                for term in terms:
                    looping(term)

def looping(variable):
    if(variable.getClass() == "Terminal"):
        print(variable.getValue())
    if (variable.getClass() == "Variable"):
        terms = variable.getRandomThing()
        for term in terms:
            looping(term)

def readerFile():
    terminals = []
    variables = []
    firstSymbol = ""
    file_ = open("grammar.txt","r")
    rows = file_.read().split('\n')
    readingWhat = "Nothing"
    for row in rows:
        # Se a linha começar com [ eu já sei que é o inicio de uma Variavel ou Terminal
        if row[0] == "[":
            # Se estiver na parte de Terminais, Variaveis ou Inicial seta para as 2 listas e a variavel.
            if readingWhat == "Terminais":
                tempRow = row.split(' ')
                terminals.append(Terminal(tempRow[1],"Masc","Sing"))
            elif readingWhat == "Variaveis":
                tempRow = row.split(' ')
                variables.append(Variable(tempRow[1],[],"None"))
            elif readingWhat == "Inicial":
                tempRow = row.split(' ')
                firstSymbol = tempRow[1]
            # Se estiver na aba Regras, modifica a entrada para facilitar a leitura
            elif readingWhat == "Regras":
                row = row.replace(' ','')
                row = row.replace('[',' ')
                row = row.replace(']',' ')
                row = row.replace('>', '')
                tempRow = row.split(' ')
                index = 0
                for variable in variables:
                    # O index é [1] porque o array é ["", "S", ">", "NP"]
                    # Quando achar a variavel que inicia a regra, aloca as outras variaveis, terminais nela
                    if tempRow[1] ==variable.getValue():
                        queijo = alocateTerms(variables, terminals, tempRow[2:], variable)
                        variable.varsTerms.append(queijo)
        else:
            # Le o arquivo e modifica a ação do loop anterior
            if row == "Terminais":
                readingWhat = "Terminais"
            elif row == "Variaveis":
                readingWhat = "Variaveis"
            elif row == "Inicial":
                readingWhat = "Inicial"
            elif row == "Regras":
                readingWhat =  "Regras"
    return variables, terminals, firstSymbol

def printVariables(variables):
    for variable in variables:
        print(variable)
        print(variable.getVarsTerms())
        #for term in variable.getVarsTerms():
            #print(term)
        print("-------------")

def alocateTerms(variables, terminals, terms, mainVar):
    # Vai ler cada termo da regra dada, ex: "[ S ] > [ NP ] [ VP ] ;1",
    # aqui só chega a partir do: ""> [ NP ] [ VP ] ;1"
    # (corto o símbolo inical que é a Variavel que já está sendo alocada)
    # Eu vejo o "nome" do termo (var, ou terminal) e procura esse nome nas listas de: variables, terminals
    # quando eu acho, eu do append nas varsTerms da variavel principal da regra
    # terminando desse jeito: S(mainVar), varsTerm(do S) = [classNP,classVP]
    tempTerms = []
    for term in terms:
        for variable in variables:
            if term == variable.getValue():
                tempTerms.append(variable)
        for terminal in terminals:
            if term == terminal.getValue():
                tempTerms.append(terminal)
    #print(tempTerms)
    return tempTerms

if __name__ == '__main__':
    # Ex: Linguagem
    variables, terminals, firstSymbol = readerFile()
    firstLooping(firstSymbol, variables)
