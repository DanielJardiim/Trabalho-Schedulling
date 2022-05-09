def circular(filaProcessos,quantum,trocaContexto):
    #Vai receber o tempo atual em que cada processo terminou a execução
    turnAround = [0] * len(filaProcessos)
    #Tamanho da fatia executada
    tempoAtual = 0

    while True:
        if sum(filaProcessos) <= 0:
            print("Todos os processos foram executados!")
            break
        else:
            for i in range(len(filaProcessos)):
                if filaProcessos[i] <= 0:
                    print(f"\nP{i} já Finalizado")
                elif filaProcessos[i] <= quantum:
                    tempoAtual += filaProcessos[i]
                    filaProcessos[i] -= filaProcessos[i]
                    print(f"\nP{i} executa")
                    print(f"Termino em T-{tempoAtual}")
                    if filaProcessos[i] == 0:
                        turnAround[i] = tempoAtual
                        print(f"Processo P{i} terminou em T-{tempoAtual}")
                        print("Troca de Contexto")
                        tempoAtual += trocaContexto
                else:
                    tempoAtual += quantum
                    filaProcessos[i] -= quantum
                    print(f"\nP{i} executa")
                    print(f"Termino em T-{tempoAtual}")
                    print("Troca de Contexto")
                    tempoAtual += trocaContexto
                    turnAround[i] = tempoAtual
            print("-" * 30)
    print(F"Tempo onde terminou cada processo: {turnAround}")
    return turnAround

def tempoAtualMedioTurnAround(listaProcessos,ListaTempos):
    resultado = sum(ListaTempos) / (len(listaProcessos))
    print(f"Tempo médio de Turn Around = {resultado:.2f}")

if __name__ == '__main__':
    filaProcessos = [53,17,68,24]
    quantum = 20
    trocaContexto = 0

    turnAround = circular(filaProcessos,quantum,trocaContexto)
    tempoAtualMedioTurnAround(filaProcessos,turnAround)