def calcular(d,q,nc,na):
    indice = 0
    if (d > 0 or q > 0) and (nc > 0 or na > 0):
        indice += (d * 2) + (q * 3.5) + (nc * 1.5) + (na * 2)
    else:
        return 0
    return indice


lista = []
for i in range(5):
    nome = input()
    desempenho = int(input())
    qntd_gols = int(input())
    nivel_cansaco = int(input())
    nivel_amizade = int(input())
    lista.append(calcular(desempenho,qntd_gols,nivel_cansaco,nivel_amizade))


def printar(li):
    for i in range(3):
        print(max(li))
        li.remove(max(li))

printar(lista)