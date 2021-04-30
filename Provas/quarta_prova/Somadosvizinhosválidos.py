ordem = int(input())
matriz = []
for i in range(ordem):
    linha = []
    elemento = input().split()
    for j in elemento:
        linha.append(int(j))
    matriz.append(linha)

soma = 0
aux = 0

for linha in range(ordem):
    for coluna in range(ordem):
        if linha != 0:
            if matriz[linha -1][coluna] >= 0:
                soma += matriz[linha-1][coluna]
                aux += 1

        if linha != ordem-1:
            if matriz[linha +1][coluna] >= 0:
                soma += matriz[linha+1][coluna]
                aux += 1

        if coluna != 0:
            if matriz[linha][coluna -1] >= 0:
                soma += matriz[linha][coluna-1]
                aux += 1

        if coluna != ordem-1:
            if matriz[linha][coluna +1] >= 0:
                soma += matriz[linha][coluna+1]
                aux += 1
print(aux)
print(soma)