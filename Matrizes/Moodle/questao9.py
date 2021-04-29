matriz = []
soma_diag = 0
soma_sec = 0

for i in range(3):
    linha = []
    elemento = input().split()
    for j in elemento:
        linha.append(int(j))
    matriz.append(linha)

print("\n")

#percorrer a diagonal principal
magico = 0
for i in range(3):
    soma_diag += matriz[i][i]

#percorrer a diagonal secundaria
for i in range(3):
    soma_sec += matriz[i][-i-1]

#percorrer as 3 linhas
for i in range(3):
    soma_lin = 0
    for j in range(3):
        soma_lin += matriz[i][j]

#percorrer as 3 colunas
for i in range(3):
    soma_col = 0
    for j in range(3):
        soma_col += matriz[j][i]

if soma_col == soma_diag == soma_lin == soma_sec:
    print("Sua matriz é uma matriz de quadrado mágico")
else:
    print("Sua matriz não é uma matriz de quadrado mágico")