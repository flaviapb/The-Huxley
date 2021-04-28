lin = int(input())
col = int(input())

matriz = []

for i in range(lin):
    linha = []
    for j in range(col):
        elemento = int(input())
        linha.append(elemento)
    matriz.append(linha)


if lin != col:
    print("A matriz nao possui traco")

else:
    soma_principal = 0
    soma_secundaria = 0
    #soma primaria
    for i in range(lin):
        soma_principal += matriz[i][i]
    #soma secundaria
    for i in range(lin):
        soma_secundaria += matriz[i][-1-i]

    print(soma_principal)
    print(soma_secundaria)

for i in matriz:
    print(*i)