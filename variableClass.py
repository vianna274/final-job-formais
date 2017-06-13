from random import randint
class Variable(): # mainVar = variavel da esquerda | |  varsTerms = terminais e variaveis do lado DIREITO
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
        lenghtTerms = len(self.getVarsTerms())
        randomTerm = self.varsTerms[randint(0, lenghtTerms-1)]
        return randomTerm

    def getClass(self):
        return "Variable"

    def __str__(self):
        return "Variable " + str(self.value)
