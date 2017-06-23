class State():

    def __init__(self,stateId, varsTerms):
        self.stateId = stateId
        self.varsTerms = varsTerms

    def getValue(self):
        return self.stateId

    def setVarsTerms(self, varTerm):
        self.varsTerms.append(varTerm)

    def getVarsTerms(self):
        return self.varsTerms
