matriz1 = []
matriz2 = []
for i in range(2):
    linha = []
    elemento = input().split()
    for j in elemento:
        linha.append(int(j))
    matriz1.append(linha)
print("\n")
for i in range(2):
    linha2 = []
    elemento2 = input().split()
    for j in elemento2:
        linha2.append(int(j))
    matriz2.append(linha2)
print("\n")
soma = []
for i in range(2):
    cont = []
    for j in range(3):
        cont.append(matriz1[i][j] + matriz2[i][j])
    soma.append(cont)

print("A soma das matrizes == {}".format(soma))