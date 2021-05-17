# --> Os dois casos funcionam
    #primeiro teste

num = input().split()
lista = []
def receber_num(num):
    for j in num:
        lista.append(int(j))

def maior_num(lista):
    maior = (lista[0] + lista[1] + abs(lista[0] - lista[1]))/2
    
    resultado = ((maior + lista[2] + abs(maior - lista[2])))/2

    print("{} eh o maior".format(int(resultado)))

receber_num(num)
maior_num(lista) 

                #segundo teste
num = input().split()

valor1, valor2, valor3 = num


def maior_num(valor1,valor2,valor3):
    maior = (int(valor1) + int(valor2) + abs(int(valor1) - int(valor2)))/2
    
    resultado = ((maior + int(valor3) + abs(maior - int(valor3))))/2

    print("{} eh o maior".format(int(resultado)))

maior_num(valor1,valor2,valor3)