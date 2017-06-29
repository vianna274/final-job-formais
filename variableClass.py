from random import randint
class Variable(): # valor = variavel da esquerda | |  varsTerms = terminais e variaveis do lado DIREITO

    def __init__(self, valor, termos):
        self.setValue(valor)
        self.varsTerms = []
        self.state = 0
        self.saw = False

    def alreadySaw(self):
        return self.saw

    def setSaw(self, saw):
        self.saw = saw

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def appendTerm(self,termos):
        self.varsTerms.append(termos)

    def setTerms (self, terms):
        self.varsTerms = terms

    def expendTerm(self,termos):
        self.varsTerms.extend(termos)

    def getVarsTerms(self):
        return self.varsTerms

    def setState(self, state):
        self.state = state

    def getDotIndex(self):
        return self.getVarsTerms().index(".")

    def dotIsFinal(self):
        if self.getDotIndex() == (len(self.getVarsTerms())-1):
            return True
        else:
            return False

    def removeDot(self):
        del self.getVarsTerms()[self.getDotIndex()]

    def setDot(self, index):
        self.getVarsTerms().insert(index, ".")

    def moveDot(self):
        self.getVarsTerms().insert(self.getDotIndex()+2,".")
        del self.getVarsTerms()[self.getDotIndex()]

    def getState(self):
        return self.state

    def getRandomThing(self): # Retorna um elemento aleatório do "varTerms"
        lenghtTerms = len(self.getVarsTerms())
        randomTerm = self.varsTerms[randint(0, lenghtTerms-1)]
        return randomTerm

    def getClass(self):
        return "Variable"

    def __str__(self):
        return " " + str(self.value)
