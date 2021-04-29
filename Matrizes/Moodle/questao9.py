matriz = []
soma_diag = 0
soma_sec = 0
soma_lin = 0
soma_col = 0
for i in range(3):
    linha = []
    elemento = input().split()
    for j in elemento:
        linha.append(int(j))
    matriz.append(linha)

print("\n")

#percorrer a diagonal principal
for i in range(3):
    soma_diag += matriz[i][i]
print(soma_diag)
#percorrer a diagonal secundaria
for i in range(3):
    soma_sec += matriz[i][-i-1]
print(soma_sec)
#percorrer as 3 linhas
#percorrer as 3 colunas

# FALTA ACABAR