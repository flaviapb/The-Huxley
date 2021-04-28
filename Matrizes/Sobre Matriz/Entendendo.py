#forma 1 de se declarar uma matriz

matriz = [[0,0,0],[0,0,0],[0,0,0]  ]
for lin in range(0, 3):
    for col in range(0, 3):
        matriz[lin][col] = int(input(f"digite um valor para [{lin},{col}] :"))
print(matriz)

print("--"*20)
print()

#forma 2 de se declarar uma matriz
matriz2 = []
for lin in range(0, 3):
    lista = []
    for col in range(0,3):
        numeros = int(input())
        lista.append(numeros)
    matriz2.append(lista)
print(matriz2)

print("--"*20)
print()

#imprimir matriz
for lin in range(0,3):
    for col in range(0,3):
        print(matriz[lin][col], end=' ')
    print()

print("--"*20)
print()

#imprimir matriz

for i in range(qtd):
    for j in range(qtd):
        if j == qtd-1:
            print(matriz[i][j])
        else:
            print(matriz[i][j], end = ' ')

print("--"*20)
print()

#percorrer diagonal principal

for i in range(3): 
   print(matriz[i][i], end=" ")

print("--"*20)
print()

#percorrer diagonal secundária
for i in range(3):
        somaSecundaria += matriz[i][-1 -i]