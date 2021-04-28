linhas, colunas = input().split()
ordem_linha = int(linhas)
ordem_coluna = int(colunas)
matriz = []

for i in range(ordem_linha):
    elementos = input().split()
    linha = []
    for j in elementos:
        linha.append(int(j))
    matriz.append(linha)
    
for i in range (ordem_coluna):
    for j in range(ordem_linha):
        print(matriz[j][i], end=" ")
    print()