matriz = []

for i in range(3):
    linha = []
    elemento = input().split()
    for j in elemento:
        linha.append(int(j))
    matriz.append(linha)

print("\n")

print("Secundaria:")
#Diagonal secundaria
for i in range(3):
    print(matriz[i][-i-1])