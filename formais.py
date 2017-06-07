#user.py
class Variable():
    mainVar = None
    varsTerms = None
    totalmenteVisitado = None
    estado = None

    def __init__(self,mainVar, varsTerms, estado):
        self.setMainVar(mainVar)
        self.varsTerms = varsTerms
        self.totalmenteVisitado = False
        self.estado = estado

    def setMainVar(self,mainVar):
        self.mainVar = mainVar
        
    def getMainVar(self):
        return self.mainVar

    def setVarsTerms(self,varsTerms):
        self.varsTerms = varsTerms

    def getVarsTerms(self):
        return self.varsTerms

    def setTotalmenteVisitado(self,totalmenteVisitado):
        self.varsTerms = totalmenteVisitado

    def getTotalmenteVisitado(self):
        return self.totalmenteVisitado

    def setEstado(self,estado):
        self.estado = estado

    def getEstado(self):
        return self.estado

if __name__ == '__main__':
    a = Variable("Exemplo de mainVar",5,'Exemplo de estado: desligado')
    print(a.getMainVar())
    print(a.getTotalmenteVisitado())
    print(a.getVarsTerms())
    print(a.getEstado())
    
    
