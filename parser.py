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
def searchDotVar(states, variable, state):
    # Pega só o "valor" da variavel para ser procurada
    value = variable.getVarsTerms()[variable.getDotIndex()+1].getValue()
    # Procura o termo direto nas regras geradas do termo 0
    for var in states[0].getVarsTerms():
        if var.getValue() == value and not var.dotIsFinal():
            if not alreadyInside(states[state].getVarsTerms(), var):
                tempVar = copyVariable(var)
                tempVar.setState(state)
                states[state].setVarsTerms(tempVar)

# Faz o início de cada estado, procura a variável que tem o terminal
# Para começar o processo do algoritmo
def firstSymbolOfGroup(states, word, state):
    found = False
    for variable in states[state-1].getVarsTerms():
        if variable == None:
            return
        if not variable.dotIsFinal():
            if variable.getVarsTerms()[variable.getDotIndex()+1].getValue() == word:
                tempAux = copyVariable(variable)
                tempAux.moveDot()
                states[state].setVarsTerms(tempAux)
                found = True
    return found

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
    # Estado atual
    stateNum = 1
    # Variavel para armazenar o dado caso não ache terminal
    varBuffer = ""
    for word in phrase:
        # Se a variavel estiver vazia quer dizer que reconheceu e procedeu o algoritmo certo, então cria um novo estado
        if varBuffer == "":
            states.append(State(stateNum,[]))
        # Se o buffer estiver com algo, ele deve ser realocado para ser reconhecido com a próxima palavra
        if varBuffer != "":
            totalPhrase = varBuffer + " " + word
            varBuffer = totalPhrase
        else:
            totalPhrase = word
        # Vai achar o primeiro elemento do Estado N (o terminal), retornará True se achou, False caso não
        foundTerminal = firstSymbolOfGroup(states, totalPhrase, stateNum)
        # Se achou, zera o buffer e começa o loop
        if foundTerminal:
            varBuffer = ""
            verifying = True
            while(verifying):
                # Recebe a próxima ação decorrente de todas as variáveis no estado atual
                opt, var = whatVerify(states, stateNum)
                print(opt)
                if opt == "Ponto Final":
                    searchFinalDot(states, stateNum, var)
                elif opt == "Ponto Variavel":
                    searchDotVar(states, var, stateNum)
                if opt == "Acabou":
                    verifying = False
            stateNum = stateNum + 1
        # Se não achou, armazena a palavra no buffer para o próximo reconhecimento
        else:
            varBuffer = word
    # Só para printar todos os estados no final da execução
    for state in states:
        print("_____")
        for x in state.getVarsTerms():
            print(x)
            print(x.getVarsTerms())
            print(x.getState())
        print("@@@@")






if __name__ == '__main__':
    variaveis, terminais, startingVar = readInput()

    states = []
    states.append(State(0, recognizationPhaseOne(variaveis)))

    recognizationPhaseTwo(["atencao","a experiencia","mostra que","o novo modelo","estrutural aqui preconizado","prejudica a percepcao","da importancia","das opcoes basicas para o sucesso do programa"], states, startingVar)
    #recognizationPhaseTwo(["dog fuck","runs"], states, startingVar)
    if(recognized(states,startingVar)):
        print("OPA DEU CERTO")
    else:
        print("COCO NAO SEI MAIS O Q ESCREVER")
