matriz = []
matriz2 = []

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

#primeiramatriz
if matriz[1][0] == 0 and matriz[2][0] == 0 and matriz[2][1] == 0:
    print("M1 é uma matriz triangular superior")
else:
    print("M1 não é uma matriz triangular superior")

#segundamatriz
if matriz2[1][0] == 0 and matriz2[2][0] == 0 and matriz2[2][1] == 0:
    print("M2 é uma matriz triangular superior")
else:
    print("M2 não é uma matriz triangular superior")