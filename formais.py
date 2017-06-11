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

def looping(P):
    if(P.getClass() == "Terminal"):
        print(P.getValue())
    if (P.getClass() == "Variable"):
        terms = P.getRandomThing()
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
        if row[0] == "[":
            if readingWhat == "Terminais":
                tempRow = row.split(' ')
                terminals.append(Terminal(tempRow[1],"Masc","Sing"))
            elif readingWhat == "Variaveis":
                tempRow = row.split(' ')
                variables.append(Variable(tempRow[1],[],"None"))
            elif readingWhat == "Inicial":
                tempRow = row.split(' ')
                firstSymbol = tempRow[1]
            elif readingWhat == "Regras":
                row = row.replace(' ','')
                row = row.replace('[',' ')
                row = row.replace(']',' ')
                row = row.replace('>', '')
                tempRow = row.split(' ')
                index = 0
                for variable in variables:
                    if tempRow[1] ==variable.getValue():
                        print(variable)
                        print(variable.getVarsTerms())
                        queijo = alocateTerms(variables, terminals, tempRow[2:], variable)
                        variable.varsTerms.append(queijo)
                        print(variable.getVarsTerms())
                        print("---")
                    index += 1
        else:
            if row == "Terminais":
                readingWhat = "Terminais"
            elif row == "Variaveis":
                readingWhat = "Variaveis"
            elif row == "Inicial":
                readingWhat = "Inicial"
            elif row == "Regras":
                readingWhat =  "Regras"

def printVariables(variables):
    for variable in variables:
        print(variable)
        print(variable.getVarsTerms())
        #for term in variable.getVarsTerms():
            #print(term)
        print("-------------")

def alocateTerms(variables, terminals, terms, mainVar):
    tempTerms = []
    for term in terms:
        for variable in variables:
            if term == variable.getValue():
                tempTerms.append(variable.getValue())
        for terminal in terminals:
            if term == terminal.getValue():
                tempTerms.append(terminal.getValue())
    #print(tempTerms)
    return tempTerms

if __name__ == '__main__':
    # Ex: Linguagem



    V = Variable("V", [[Terminal("dos tempos", "Plural", "Masculino")], [Terminal("das cidades", "Plural", "Feminino")], [Terminal("das vidas", "Plural", "Masculino")]], "Sei La")
    R = Variable("R", [[Terminal("os homens", "Plural", "Masculino")],[Terminal("as mulheres", "Plural", "Feminino")]], "Sei La")
    J = Variable("J", [[Terminal("deram o popo", "Plural", "Masculino")]], "Sei La")
    Y = Variable("Y", [[Terminal("O inicio", "Singular", "Neutro")]], "Sei La")
    P = Variable("P",[[Y, V, R, J,], [Terminal("Ops hehe", "Singular", "Neutro")]], "Inicio")

    readerFile()
