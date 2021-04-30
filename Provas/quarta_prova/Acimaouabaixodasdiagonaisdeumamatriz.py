lugar = str(input()).lower()
num = int(input())

ordem = int(input())
matriz = []
for i in range(ordem):
    linha = []
    elemento = input().split()
    for j in elemento:
        linha.append(int(j))
    matriz.append(linha)

if lugar == "acima":
    soma = 0
    cont = 1
    for i in range(0,ordem-1):
        for j in range(cont,ordem):
            soma += matriz[i][j]
        cont += 1
    if soma > num:
        print("True")
    else:
        print("False")

if lugar == "abaixo":
    soma = 0
    cont = ordem - 1
    for i in range(ordem-1,0,-1):
        for j in range(0,cont):
            soma += matriz[i][j]
        cont -= 1
    print(soma)
    if soma > num:
        print("True")
    else:
        print("False")
