ordem = int(input())
matriz = []

for i in range(ordem):
    cont = 1
    linha = []
    for j in range(ordem):
        linha.append(cont)
        cont += 1
    matriz.append(linha)

cont = -1 
for i in range(ordem):
    for j in range(ordem):
        if j == ordem-1 and j > cont:
            print(matriz[i][j])
        elif j > cont:
            print(matriz[i][j], end=' ')
        else:
            print(" ", end=' ')
    cont += 1