                                            "Desenvolvido por Flávia"

qntd = input()
num = input().split()
lista= []
lista1 = []
pontos = 0

for i in num:
    if i not in lista1:
        lista1 = lista
        lista = []
        lista1.append(i)
    else:
        lista1.append(i)

    if len(lista1) > pontos:
        pontos = len(lista1)

print(pontos)