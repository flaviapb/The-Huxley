linhas, colunas = input().split()
ordem_linha = int(linhas)
ordem_coluna = int(colunas)
matriz = []

for i in range(ordem_linha):
    linha = []
    for c in range(ordem_coluna):
        elemento = int(input())
        linha.append(elemento)
    matriz.append(linha)

#Printar matriz sem colchetes e virgulas
print("Matriz formada:")
for i in matriz:
    print(*i)
    
#soma de primárias e secundária
while True:
    primaria = 0
    secundaria = 0
    if ordem_linha != ordem_coluna:
        print("A diagonal principal e secundaria nao pode ser obtida.")
        break
    else:
        if ordem_linha == ordem_coluna:
            for i in range(ordem_linha):
                primaria += matriz[i][i]
            for j in range(ordem_linha):
                secundaria += matriz[j][-1 -j]

            print("A diagonal principal e secundaria tem valor(es) {} e {} respectivamente.".format(primaria,secundaria))
            break
    
#maior e menor que 0
maior = 0
menor = 0
for i in range(ordem_linha):
    for j in range(ordem_coluna):
        if matriz[i][j] < 0:
            menor += 1
        else:
            maior += 1

print("A matriz possui {} numero(s) menor(es) que zero.".format(menor))

print("A matriz possui {} numero(s) maior(es) que zero.".format(maior)) 