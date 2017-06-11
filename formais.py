#user.py
from random import randint

class GeneralClass():
    value = None
    varsTerms = None
    totalmenteVisitado = None
    estado = None

    # mainVar = variavels da esquerda
    # mainVar = variavel da esquerda
    # varsTerms = lista de tuplas [(V, "var"),("*", "ponto") (R,"var"), ("oi","term")]
    def __init__(self, value, varsTerms, estado):
        self.setValue(value)
        self.setVarsTerms(varsTerms)
        self.setTotalmenteVisitado(False)
        self.setEstado(estado)

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def setVarsTerms(self,varsTerms):
        self.varsTerms = varsTerms

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
    def __init__(self,mainVar, varsTerms, estado):
        GeneralClass.__init__(self,mainVar, varsTerms, estado)
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
if __name__ == '__main__':
