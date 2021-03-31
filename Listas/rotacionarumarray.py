qntd = int(input())
lista = []

for i in range(qntd):
     num = int(input())
     lista.append(num)

pulo = int(input())

for i in range(pulo,qntd):
     print(lista[i])

for i in range(pulo):
     print(lista[i])

