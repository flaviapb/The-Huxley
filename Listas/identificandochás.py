tipo = int(input())
lista_acertos = []

for i in range(5):
    lista_acertos = input().split()
    break


for i in range(5):
    lista_acertos[i] = int(lista_acertos[i])

    cont = lista_acertos.count(tipo)
    

print(cont)

