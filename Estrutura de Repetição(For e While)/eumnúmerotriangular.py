"Desenvolvido por Flávia"

num = int(input())

cont = 1

while cont * (cont + 1) * (cont + 2) < num:
    cont += 1

if cont * (cont+1) * (cont+2) == num:
    print("{} * {} * {} = {}".format(cont,cont+1,cont+2,num))
    print("Verdadeiro")

else:
    print("Falso")