matriz = []

for i in range(3):
    linha = []
    elemento = input().split()
    for j in elemento:
        linha.append(int(j))
    matriz.append(linha)

print("\n")

print("Principal: ")
#Diagonal principal
for i in range(3):
    print(matriz[i][i])


