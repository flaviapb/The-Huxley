matriz = []
matriz2 = []
matriz3 = []
for i in range(3):
    linha = []
    elemento = input().split()
    for j in elemento:
        linha.append(int(j))
    matriz.append(linha)

print("\n")

for i in range(3):
    linha2 = []
    elemento2 = input().split()
    for j in elemento2:
        linha2.append(int(j))
    matriz2.append(linha2)

print("\n")

for i in range(3):
    linha3 = []
    for j in range(3):
        if matriz[i][j] == matriz2[i][j]:
            linha3.append(matriz2[i][j])
        elif matriz[i][j] != matriz2[i][j]:
            linha3.append(0)
    matriz3.append(linha3)

#pode imprimir assim
for i in range(3):
    for j in range(3):
        print(matriz3[i][j], end=" ")
    print()

print("\n")

#ou assim
for i in matriz3:
    print(*i)