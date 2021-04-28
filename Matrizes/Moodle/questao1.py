matriz = [[1,2,4],[8,10,12],[21,24,27]]
linha = int(input("Digite sua linha para soma: "))
coluna = int(input("Digite sua coluna para soma: "))
soma = matriz[linha][coluna]

if linha != 0:
    soma += matriz[linha-1][coluna]

if linha != 2:
    soma += matriz[linha+1][coluna]

if coluna != 0:
    soma += matriz[linha][coluna-1]

if coluna != 2:
    soma += matriz[linha][coluna+1]

print("\n")

for l in matriz:
    print(l)

print("\n")
print("A soma referente a linha {} e coluna {}: {}".format(linha,coluna,soma))