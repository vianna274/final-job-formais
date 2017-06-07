class Variable:
    # mainVar = variavel da esquerda
    # varsTerms = lista de tuplas [("V", "var"),("*", "ponto") ("R","var"), ("oi","term")]
    def __init__(mainVar, varsTerms, estado):
        self.mainVar = mainVar
        self.varsTerms = varsTerms
        self.totalmenteVisitado = False
        self.estado = estado
