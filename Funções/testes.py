#Sem parâmetros

def pula_linha():
    print("\n")

def mostra_linha():
    print("-"*30)

mostra_linha()
print("Meu nome é Flávia")
pula_linha()
print("Tenho 18 anos")
pula_linha()
print("Tchauzin")
mostra_linha()

pula_linha()

                                            #Com parâmetros

def mensagem(msg):
    print("-"*30)
    print(msg)
    print("-"*30)

mensagem("ME CHAMO FLÁVIA")
pula_linha()
mensagem("EU TE AMO")

pula_linha()

                                            #Praticando

def soma(a,b):
    print("A = {} e B = {}".format(a,b))
    print("A soma entre A e B = {}".format(a+b))
# Com um input
soma(3, b=int(input("Digite um número: ")))
mostra_linha()
# com dois input
soma(a=int(input("Digite um número: ")),b=int(input("Digite um número: ")))
mostra_linha()
#definindo os valores
soma(10,3)

                                            #Desempacotamento

def contador(*num):  #Aqui eu falo pro python, que vou receber n valores(*) função interna do python
    cont = len(num)
    print(num)
    print("A quantidade de números do contador é: {}".format(cont))

mostra_linha()
contador(3,2,1,4)
contador(2,4,5)
contador(2,2)
contador(1)
mostra_linha()

                                                #Praticando
                            #Ter uma lista e mostra ela com valores dobrados (valores definidos)

pula_linha()

def dobrando_valores(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

mostra_linha()
lista = [2,4,6]
print("Original: {}".format(lista))
dobrando_valores(lista)
print("Dobrada: {}".format(lista))
mostra_linha()


                                    #Entendendo o return

def soma():  #defini a função
    return 10  #falei que a função retorna o número 10

num = soma() #falei que minha variavel reecebia minha função
print( num ) #printa a variavel, ou seja, a função

if num > 10:
    print("oi")
else:
    print("tchau")

       

