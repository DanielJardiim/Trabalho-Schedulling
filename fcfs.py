#Calcular Waiting Time
def waitingTime(processos):
    #Definindo a quantidade tempo de serviço de cada, baseado na qnt. de processos.
    tempoServico = [0] * len(processos)
    #O tempo de serviço é a somade todos os Burst Time dos processos anteriores.
    tempoServico[0] = 0
    #Definindo tamanho da waiting list
    wt = [0] * len(processos)

    for i in range(1,len(processos)):
        tempoServico[i] = (tempoServico[i-1] + processos[i-1][1])
        wt[i] = tempoServico[i] - processos[i][0]
        if wt[i] < 0 :
            wt[i] = 0
    return wt

#Calcular Turn Around Time
def turnAroundTime(processos):
    #Turn Around Time = Burst Time + Waiting Time
    tat = [0] * len(processos) #Turn Around Time
    wt = waitingTime(processos)
    for i in range(len(processos)):
        tat[i] = processos[i][1] + wt[i]
    return tat

#Calcular media do Waiting Time
def averageWaitingTime(processos):
    qntProc = len(processos)
    wt = sum(waitingTime(processos))
    return (wt / qntProc)

#Calcular media da Turn Around Time
def averageTurnAroundTime(processos):
    qntProc = len(processos)
    tat = sum(turnAroundTime(processos))
    return (tat / qntProc)

#Calcular media da Completion Time
def averageCompletionTime(processos):
    qntProc = len(processos)
    ct = 0
    for proc in range(len(processos) - 1):
        ct = ct + turnAroundTime(processos)[proc] + processos[proc][0]
    return (ct / qntProc)

#Lista de todos os processos
processos = []
qntProcessos = int(input("Quantidade de Processos: "))
for i in range(qntProcessos):
    arrivalTime = int(input("Arrival Time: "))
    burstTime = int(input("Burst Time: "))
    print(" ")
    processos.append([arrivalTime,burstTime])

"""
Estrutura do Processo
[[arrivalTime,burstTime]]
"""

print("Process\tBurst Time\tArrival Time\tWaiting Time\tTurn Around Time\tCompletion Time\n\n")
wt = waitingTime(processos)
tat = turnAroundTime(processos)
avgWt = averageWaitingTime(processos)
avgTat = averageTurnAroundTime(processos)
avgCt = averageCompletionTime(processos)
#Completion Time = Turn Around Time + Arrival Time
for proc in range(len(processos)):
    print(f"{proc}\t\t{processos[proc][1]}\t\t{processos[proc][0]}\t\t{wt[proc]}\t\t{tat[proc]}\t\t{tat[proc] + processos[proc][0]}\n")
print(f"Average Waiting Time : {avgWt}")
print(f"Average Turn Around Time : {avgTat}")
print(f"Average Completion Time : {avgCt}")