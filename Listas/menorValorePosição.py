'refazer'


numeros = []
vezes = int(input())

for i in range(vezes):
    numeros = input().split()
    #numeros[i] = int(numeros[i])
    #numeros.append(num)
    break

for i in range(vezes):
    numeros[i] = int(numeros[i])



print("Menor valor: {}".format(min(numeros)))
print("Posicao: {}".format(numeros.index(min(numeros))))