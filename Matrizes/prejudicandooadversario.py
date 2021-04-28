ordem = int(input())
matriz = []

for i in range(ordem):
    elemento = input().split()
    linha = []
    for c in elemento:
        linha.append(int(c))
    matriz.append(linha)

for i in range (ordem):
    for j in range(ordem):
        if matriz[j][i] < 0:
            matriz[j][i] *= 2
            if j == ordem-1: 
                print(matriz[j][i])
            else:
                print(matriz[j][i], end=" ")
        else:
            if j == ordem-1: 
                print(matriz[j][i])
            else:
                print(matriz[j][i], end=" ")
