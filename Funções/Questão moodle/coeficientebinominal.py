n = int(input("Digite o valor de n: "))
k = int(input("Digite o valor de k: "))

def fatorial(x):  #fatorando os valores
    total = 1
    for N in range(x):
        total = total * (N + 1)
    return total


def calculandoBinomial(n,k):   #calculando o binominal 
   return fatorial(n) / (fatorial(k) * fatorial(n-k))

def validando(n,k):   #validando o binominal 
    if k > n:
        return 0
    else:
        return calculandoBinomial(n,k)


def printar():  # printar o binominal 
    print("\nCalculando os números binomiais\n")
    print("Entre os números {} e {} é : {}".format(n,k,int(validando(n,k))))

printar()  # chamando a função para printar o número binominal