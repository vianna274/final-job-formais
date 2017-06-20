# -*- coding: utf-8 -*-
import re
from input import *
import os
import os.path


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
        # Procura o termo da esquerda no estado logo após o /
        for variable in states[mainVariable.getState()].getVarsTerms():
            if not variable.dotIsFinal():
                if variable.getVarsTerms()[variable.getDotIndex()+1].getValue() == value and not alreadyInside(states[state].getVarsTerms(),variable):
                    tempVar = copyVariable(variable)
                    tempVar.moveDot()
                    states[state].setVarsTerms(tempVar)
        mainVariable.setSaw(True)

# Recebe todos os estados, o estado atual e a Variavel que vai ser procurada
# Atualiza a lista States, atualizando o estado atual
def searchDotVar(states, variable, state, unknownState):
    # Pega só o "valor" da variavel para ser procurada
    value = variable.getVarsTerms()[variable.getDotIndex()+1].getValue()
    # Procura o termo direto nas regras geradas do termo 0
    for var in unknownState.getVarsTerms():
        if var.getValue() == value and not var.dotIsFinal():
            if not alreadyInside(states[state].getVarsTerms(), var):
                tempVar = copyVariable(var)
                tempVar.setState(state)
                states[state].setVarsTerms(tempVar)

# Faz o início de cada estado, procura a variável que tem o terminal
# Para começar o processo do algoritmo
def firstSymbolOfGroup(states, word, state):
    #print("WORD = " + word)
    found = False
    for variable in states[state-1].getVarsTerms():
        #print("VAR = " + variable.getValue())
        #print("VARDOT = " + str(variable.dotIsFinal()))
        if variable == None:
            return
        if not variable.dotIsFinal():
            if variable.getVarsTerms()[variable.getDotIndex()+1].getValue() == word:
                tempAux = copyVariable(variable)
                tempAux.moveDot()
                states[state].setVarsTerms(tempAux)
                found = True
    return found

# Faz o grupo 0 a partir da variavel inicial
def firstVarOfGroup(states, unknownState, firstVar):
    for variable in unknownState.getVarsTerms():
        if variable.getValue() == firstVar:
            tempAux = copyVariable(variable)
            states[0].setVarsTerms(tempAux)
    verifying = True
    while(verifying):
        # Recebe a próxima ação decorrente de todas as variáveis no estado atual
        opt, var = whatVerify(states, 0)
        print(opt)
        if opt == "Ponto Final":
            searchFinalDot(states, 0, var)
        elif opt == "Ponto Variavel":
            searchDotVar(states, var, 0, unknownState)
        if opt == "Acabou":
            verifying = False

# Faz o grupo 0 a partir da variavel inicial
def firstVarOfGroup(states, unknownState, firstVar):
    for variable in unknownState.getVarsTerms():
        if variable.getValue() == firstVar:
            tempAux = copyVariable(variable)
            states[0].setVarsTerms(tempAux)
    verifying = True
    while(verifying):
        opt, var = whatVerify(states, 0)
        if opt == "Ponto Final":
            searchFinalDot(states, 0, var)
        elif opt == "Ponto Variavel":
            searchDotVar(states, var, 0, unknownState)
        if opt == "Acabou":
            verifying = False

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

def alreadyInsideWithDots(variables, variableAux):
    for variable in variables:
        if variable.getValue() == variableAux.getValue() and variable.getVarsTerms() == variableAux.getVarsTerms():
            return True
    else:
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
    #print("\nINICIAL: " + startSymbol)
    for var in states[len(states)-1].getVarsTerms():
        #print("VAR = " + var.getValue())
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
def recognizationPhaseTwo(phrase, states, firstVar, unknownState):
    firstVarOfGroup(states, unknownState, firstVar)
    # Estado atual
    stateNum = 1
    # Variavel para armazenar o dado caso não ache terminal
    for word in phrase:
        states.append(State(stateNum, []))
        # Vai achar o primeiro elemento do Estado N (o terminal), retornará True se achou, False caso não
        foundTerminal = firstSymbolOfGroup(states, word, stateNum)
        if not foundTerminal:
            return
        # Se achou, zera o buffer e começa o loop
        verifying = True
        while(verifying):
            # Recebe a próxima ação decorrente de todas as variáveis no estado atual
            opt, var = whatVerify(states, stateNum)
            #print(opt)
            if opt == "Ponto Final":
                searchFinalDot(states, stateNum, var)
            elif opt == "Ponto Variavel":
                searchDotVar(states, var, stateNum, unknownState)
            if opt == "Acabou":
                verifying = False
        stateNum = stateNum + 1

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

def mainFunction():
        CHECK = "1"
        EXIT = "2"
        while True:
            option = input("Digite: \n\n1 - Checar string\n2 - Sair\n\n>")

            if option == (EXIT):
                break

            elif option == (CHECK):
                print("Escreva a sentença a ser testada na gramatica e os terminais compostos entre " " \"\"")
                inputFile = input("\nArquivo da gramatica: ")
                inputString = input("\nString a ser checada: ")

                if os.path.exists(str(inputFile)):
                    variaveis, terminais, firstVar = readInput(str(inputFile))

                    states = []
                    unknownState = State(0, recognizationPhaseOne(variaveis))
                    states.append(State(0,[]))

                    recognizationPhaseTwo(listarPalavras(str(inputString)), states, firstVar, unknownState)

                    printStates(states)
                    if(recognized(states, firstVar)):
                        print("\n>>>> RECONHECIDO")
                    else:
                        print("\n>>>> NAO RECONHECIDO")
                    input('Pressione qualquer tecla para continuar')
                    cleanScreen()

                else:
                    input("\n!Nome de arquivo invalido!\nPressione qualquer tecla e digite uma operacao valida!")
                    cleanScreen()
            else:

                input("!Opcao invalida!\nPressione qualquer tecla e digite uma operacao valida!")
                cleanScreen()


if __name__ == '__main__':
    mainFunction()
