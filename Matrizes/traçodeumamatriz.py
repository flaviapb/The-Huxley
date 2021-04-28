ordem = int(input())
matriz = []
soma = 0

for i in range(ordem):
    elemento = input().split()
    linha = []
    for j in elemento:
        linha.append(float(j))
    matriz.append(linha)

for i in range(ordem):
    soma += matriz[i][i]

print('tr(A) = ', end='')

for i in range(ordem):
    if i == ordem-1:
        print("({:.2f}) = {:.2f}".format(matriz[i][i],soma))
    else:
        print("({:.2f}) + ".format(matriz[i][i]), end="")