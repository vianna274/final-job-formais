class Variable:
        
	mainVar = None
	varsTerms = None
	totalmenteVisitado = None
	estado = None
    # mainVar = variavel da esquerda
    # varsTerms = lista de tuplas [("V", "var"),("*", "ponto") ("R","var"), ("oi","term")]
    
    def __init__(mainVar, varsTerms, estado):
            
            self.mainVar = mainVar
            self.varsTerms = varsTerms
            self.totalmenteVisitado = False
            self.estado = estado

            
          
    def setmainVar(self,mainVar):
            self.mainVar = mainVar
    
        
