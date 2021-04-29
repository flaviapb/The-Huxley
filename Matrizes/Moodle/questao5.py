matriz = []

for i in range(3):
    linha = []
    for j in range(4):
        elemento = int(input())
        linha.append(elemento)
    matriz.append(linha)

print("\nMatriz:")
for i in matriz:
    print(*i)

print("\nMatriz transposta:")
for i in range(4):
    for j in range(3):
        print(matriz[j][i], end=" ")
    print()
