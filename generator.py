# -*- coding: utf-8 -*-
import re
#import web
from input import *
import os
import os.path

"""                AUXILIARES                   """
# Recebe uma variavel e retorna uma cópia dela
# Serve para tirar os ponteiros do mesmo lugar
urls = ('/generate/', 'gen')
phrase = ""

# Copia uma variavel
def copyVariable(variable):
    tempVar = Variable(variable.getValue(), [])
    tempVar.expendTerm(variable.getVarsTerms())
    tempVar.setState(variable.getState())
    return tempVar

# Verifica se uma variableAux já está dentro das variables
def alreadyInsideWithDots(variables, variableAux):
    for variable in variables:
        if variable.getValue() == variableAux.getValue() and variable.getState() == variableAux.getState() and variable.getVarsTerms():
            if sameVarTerms(variable, variableAux):
                return True
    else:
        return False

# Verifica se os termos da variable1 são iguais da variable2
def sameVarTerms(variable1, variable2):
    if len(variable1.getVarsTerms()) != len(variable2.getVarsTerms()):
        return False
    else:
        for index in range(1,len(variable1.getVarsTerms())):
            if variable1.getVarsTerms()[index] == "." or variable2.getVarsTerms()[index] == ".":
                pass
            elif variable1.getVarsTerms()[index].getValue() != variable2.getVarsTerms()[index].getValue():
                return False
    return True

# Recebe todos os estados e o número do estado atual
# Verifica todas as variaveis do atual estado para saber qual o próximo passo
def whatVerify(states, state):
    variables = states[state].getVarsTerms()
    for variable in variables:
        index = variables.index(variable)
        if variable == None:
            return "Frase Errada", "Error"

        elif(variable.dotIsFinal() and not variable.alreadySaw()):
            variable.setSaw(True)
            return "Ponto Final", variable

        if (not variable.dotIsFinal() and not variable.alreadySaw()):
            if (variable.getVarsTerms()[variable.getDotIndex()+1].getClass() == "Variable"):
                variable.setSaw(True)
                return "Ponto Variavel", variable
    return "Acabou", "Error"

def listarPalavras(frase):
    s = frase

    lis = re.findall(r'\"(.*?)\"', s)
    for x in lis:
        s = s.replace('"' + x + '"',x.replace(' ','-'))

    s = s.split()
    for i in range(0,len(s)):
        if '-' in s[i]:
            s[i] = s[i].replace('-',' ')
    return s

# Printa todos os estados na tela bonitinho
def printStates(states):
    for state in states:
        print("---- ESTADO " + str(state.getValue()) + " ----")
        for variable in state.getVarsTerms():
            print(variable, end=" --> ")
            for term in variable.getVarsTerms():
                print(term, end=" ")
            print("", end="\n")

def cleanScreen():
    if os.name == 'nt':
        os.system('CLS')
    else:
        os.system('clear')

# Verifica se tem ". Terminal"
def hasDotTerminal(variable):
    if variable.dotIsFinal():
        return False
    elif variable.getVarsTerms()[variable.getDotIndex()+1].getClass() == "Terminal":
        return True
    else:
        return False

# Verifica se em um estado existe alguma variável com ". estado"
def hasAnyDotTerminal(state):
    for variable in state.getVarsTerms():
        if hasDotTerminal(variable):
            return True
    return False

# Recebe uma lista de Variaveis e Terminais e retorna um randomicamente utilizando as porcentagem
def getRandomSomething(varsTerms):
    chance = 0
    prob = 0
    varAux = None
    for varTerm in varsTerms:
        prob += int(varTerm.getVarsTerms()[0]*100)

    prob = randint(0,prob)
    for varTerm in varsTerms:
        chance += int(varTerm.getVarsTerms()[0]*100)
        if prob <= chance:
            return varTerm

# Faz o grupo 0 a partir da variavel inicial
def mountGroupZero(states, unknownState, firstVar):
    for variable in unknownState.getVarsTerms():
        if variable.getValue() == firstVar and not alreadyInsideWithDots(states[0].getVarsTerms(), variable):
            tempAux = copyVariable(variable)
            states[0].setVarsTerms(tempAux)
    verifying = True
    while(verifying):
        # Recebe a próxima ação decorrente de todas as variáveis no estado atual
        opt, var = whatVerify(states, 0)
        if opt == "Ponto Final":
            searchFinalDot(states, 0, var)
        elif opt == "Ponto Variavel":
            searchDotVar(states, var, 0, unknownState)
        if opt == "Acabou" or opt == "Frase Errada":
            verifying = False

# Coloca o terminal do state X no state X+1 para iniciar o early
def getTerminal(states, state):
    for varTerm in states[state].getVarsTerms():
        if hasDotTerminal(varTerm):
            tempAux = copyVariable(varTerm)
            tempAux.moveDot()
            states[state+1].setVarsTerms(tempAux)
            return varTerm.getVarsTerms()[varTerm.getDotIndex()+1].getValue()
    return "Error"

"""                RECONHECIMENTO                 """
# Faz o primeiro loop para encher o estado 0 com todas as regras
def recognizationPhaseOne(variables):
    unknownState = []
    currentState = 0
    for variable in variables:
        for term in variable.getVarsTerms(): # getVarsTerms()[1:] -> Assim a mágica onde ignora as probabilidades (considera um vetor a partir do indice 1: em diante)
            withDot = [term[0]]
            withDot.extend(".")
            withDot.extend(term[1:])
            tempVar = Variable(variable.getValue(), [])
            tempVar.expendTerm(withDot)
            tempVar.setState(0)
            unknownState.append(tempVar)
    return unknownState

# Leia, cansei de documentar
def recognizationPhaseTwo(states, firstVar, unknownState):
    global phrase
    mountGroupZero(states, unknownState, firstVar)
    # Estado atual
    stateNum = 1
    while(hasAnyDotTerminal(states[stateNum-1])):
        states.append(State(stateNum, []))
        word = getTerminal(states, stateNum-1)
        phrase = phrase + word + " "
        verifying = True
        while(verifying):
            # Recebe a próxima ação decorrente de todas as variáveis no estado atual
            opt, var = whatVerify(states, stateNum)
            if opt == "Ponto Final":
                searchFinalDot(states, stateNum, var)
            elif opt == "Ponto Variavel":
                searchDotVar(states, var, stateNum, unknownState)
            if opt == "Acabou":
                verifying = False
        stateNum = stateNum + 1

"""                   REGRAS                      """

# Recebe a variavel que vai ser buscada
def searchFinalDot(states, state, mainVariable):
    # Pega só o "valor" da variavel para ser procurada
    tempVars = []
    value = mainVariable.getValue()
    # Procura o termo da esquerda no estado logo após o /
    for variable in states[mainVariable.getState()].getVarsTerms():
        if not variable.dotIsFinal():
            if variable.getVarsTerms()[variable.getDotIndex()+1].getValue() == value and not alreadyInsideWithDots(states[state].getVarsTerms(),variable):
                tempVar = copyVariable(variable)
                tempVar.moveDot()
                tempVars.append(tempVar)
    random = getRandomSomething(tempVars)
    if (random != None):
        states[state].setVarsTerms(random)

# Recebe todos os estados, o estado atual e a Variavel que vai ser procurada
# Atualiza a lista States, atualizando o estado atual
def searchDotVar(states, variable, state, unknownState):
    # Pega só o "valor" da variavel para ser procurada
    value = variable.getVarsTerms()[variable.getDotIndex()+1].getValue()
    # Aloca uma lista de variaveis temporarias
    tempVars = []
    # Procura a variavel direto do estado "unknown" o qual não tem estado
    for var in unknownState.getVarsTerms():
        if var.getValue() == value:
            tempVar = copyVariable(var)
            tempVar.setState(state)
            # Se o state não tiver uma variável identica da append na tempVars
            if not alreadyInsideWithDots(states[state].getVarsTerms(), tempVar):
                tempVars.append(tempVar)
    # Pega uma variavel, ou terminal randomicamente
    random = getRandomSomething(tempVars)
    if (random != None):
        states[state].setVarsTerms(random)

# Recebe os estados e o SimboloInicial, se no último estado tiver o SimboloInicial com o ponto no Final
# E no estado 0 será aceito como palavra
def recognized(states, startSymbol):
    for var in states[
        len(states)-1].getVarsTerms():
        if (var.getValue() == startSymbol and var.dotIsFinal() and var.getState() == 0):
            return True
    return False


"""                   MENU                      """
def mainFunction():
    variaveis, terminais, firstVar = readInput("sample.txt")
    states = []
    unknownState = State(0, recognizationPhaseOne(variaveis))
    states.append(State(0,[]))
    recognizationPhaseTwo(states, firstVar, unknownState)
    printStates(states)
    print(phrase)

if __name__ == '__main__':
    #app = web.application(urls, globals())
    #app.run()
    #mainFunction()
    mainFunction()
