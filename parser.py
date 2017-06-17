from input import *
import time

# Recebe uma variavel e retorna uma cópia dela
# Serve para tirar os ponteiros do mesmo lugar
def copyVariable(variable):
    tempVar = Variable(variable.getValue(), [])
    tempVar.expendTerm(variable.getVarsTerms())
    tempVar.setState(variable.getState())
    return tempVar

# Faz o primeiro loop para encher o estado 0 com todas as regras
def recognizationPhaseOne(variables):
    stateZero = []
    currentState = 0
    for variable in variables:
        for term in variable.getVarsTerms():
            withDot = list(".") + term
            tempVar = Variable(variable.getValue(), [])
            tempVar.expendTerm(withDot)
            tempVar.setState(0)
            stateZero.append(tempVar)
    return stateZero


# Recebe a variavel que vai ser buscada
def searchFinalDot(states, state, mainVariable):
    # Pega só o "valor" da variavel para ser procurada
    value = mainVariable.getValue()
    if not mainVariable.alreadySaw():
        # Procura no estado anterior se tem alguém com o ponto anterior a variavel que esta sendo buscada
        # Ex: T -> F. /0  @@ No anterior tem E -> .T * F /0, daí atualiza o estado com E -> T . * F /0
        for variable in states[state-1].getVarsTerms():
            if not variable.dotIsFinal():
                if variable.getVarsTerms()[variable.getDotIndex()+1].getValue() == value and not alreadyInside(states[state].getVarsTerms(),variable):
                    tempVar = copyVariable(variable)
                    tempVar.moveDot()
                    states[state].setVarsTerms(tempVar)

        # Faz o mesmo para o estado "nativo" da variavel
        for variable in states[mainVariable.getState()].getVarsTerms():
            if not variable.dotIsFinal():
                if variable.getVarsTerms()[variable.getDotIndex()+1].getValue() == value and not alreadyInside(states[state].getVarsTerms(),variable):
                    tempVar = copyVariable(variable)
                    tempVar.moveDot()
                    states[state].setVarsTerms(tempVar)
        mainVariable.setSaw(True)

# Recebe todos os estados, o estado atual e a Variavel que vai ser procurada
# Atualiza a lista States, atualizando o estado atual
def searchDotVar(states, variable, state):
    # Pega só o "valor" da variavel para ser procurada
    value = variable.getVarsTerms()[variable.getDotIndex()+1].getValue()
    # Procura se a variável está no indice anterior sucedendo um ponto
    # Ex: mainVariavel = T, e dai no termo anterior tem S = Q . T, então botaria S no novo estado
    for var in states[state-1].getVarsTerms():
        if var.getValue() == value and not var.dotIsFinal():
            tempVar = copyVariable(var)
            states[state].setVarsTerms(tempVar)
    # Procura também no estado nativo da variavel, se a variavel que está sendo procurada
    # foi criada no estado 1, vai ser procurada no estado 1. EVITANDO CÓPIAS
    for var in states[0].getVarsTerms():
        if var.getValue() == value and not var.dotIsFinal():
            if not alreadyInside(states[state].getVarsTerms(), var):
                tempVar = copyVariable(var)
                tempVar.setState(state)
                states[state].setVarsTerms(tempVar)

# Faz o início de cada estado, procura a variável que tem o terminal
# Para começar o processo do algoritmo
def firstSymbolOfGroup(states, word, state):
    for variable in states[state-1].getVarsTerms():
        if variable == None:
            return
        if not variable.dotIsFinal():
            if variable.getVarsTerms()[variable.getDotIndex()+1].getValue() == word:
                tempAux = copyVariable(variable)
                tempAux.moveDot()
                states[state].setVarsTerms(tempAux)

# Verifica se um termo já está dentro do array ignorando os pontos
def alreadyInside(variables, variableAux):
    dotIndAux = variableAux.getDotIndex()
    variableAux.removeDot()

    for variable in variables:
        dotInd = variable.getDotIndex()
        variable.removeDot()
        if variable.getValue() == variableAux.getValue() and variable.getVarsTerms() == variableAux.getVarsTerms():
            variable.setDot(dotInd)
            variableAux.setDot(dotIndAux)
            return True
        variable.setDot(dotInd)
    else:
        variableAux.setDot(dotIndAux)
        return False

# Verifica se 2 variaveis são iguais (tem redundância com a anteior, mas cansei de arrumar)
def sameVariable(A, B):
    AAux = A.getDotIndex()
    A.removeDot()
    BAux = B.getDotIndex()
    B.removeDot()

    if A.getValue() == B.getValue() and A.getVarsTerms() == B.getVarsTerms():
        A.setDot(AAux)
        B.setDot(BAux)
        return True

    A.setDot(AAux)
    B.setDot(BAux)
    return False

# Recebe os estados e o SimboloInicial, se no último estado tiver o SimboloInicial com o ponto no Final
# E no estado 0 será aceito como palavra
def recognized(states, startSymbol):
    for var in states[len(states)-1].getVarsTerms():
        if (var.getValue() == startSymbol and var.dotIsFinal() and var.getState() == 0):
            return True
    return False

# Recebe todos os estados e o número do estado atual
# Verifica todas as variaveis do atual estado para saber qual o próximo passo
def whatVerify(states, state):
    variables = states[state].getVarsTerms()
    for variable in variables:
        index = variables.index(variable)
        if variable == None:
            return "Frase Errada", "Error"

        elif(variable.dotIsFinal() and not variable.alreadySaw()):
            return "Ponto Final", variable

        if (not variable.dotIsFinal() and not variable.alreadySaw()):
            if (variable.getVarsTerms()[variable.getDotIndex()+1].getClass() == "Variable"):
                variable.setSaw(True)
                return "Ponto Variavel", variable

    return "Acabou", "Error"


# Leia, cansei de documentar
def recognizationPhaseTwo(phrase, states, firstSymbol):
    stateNum = 1
    for word in phrase:
        states.append(State(stateNum,[]))
        firstSymbolOfGroup(states, word, stateNum)
        verifying = True
        while(verifying):
            opt, var = whatVerify(states, stateNum)
            #print(opt)
            if opt == "Ponto Final":
                searchFinalDot(states, stateNum, var)
            elif opt == "Ponto Variavel":
                searchDotVar(states, var, stateNum)
            elif opt == "Frase Errada" or opt == "Acabou":
                verifying = False
            for state in states:
                print("_____")
                for x in state.getVarsTerms():
                    print(x)
                    print(x.getVarsTerms())
                    print(x.getState())
                print(word)
                print("@@@@")
            time.sleep(2)
        stateNum = stateNum + 1





if __name__ == '__main__':
    variaveis, terminais, startingVar = readInput()

    states = []
    states.append(State(0, recognizationPhaseOne(variaveis)))

    recognizationPhaseTwo(["X", "+", "X"], states, startingVar)
    if(recognized(states,startingVar)):
        print("OPA DEU CERTO")
    else:
        print("COCO NAO SEI MAIS O Q ESCREVER")
    #print(searchTermAfterDot(stateZero,stateZero, "X", 0))
