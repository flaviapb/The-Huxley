jogada_paes = []
paes = input().split()
for i in paes:
    jogada_paes.append(int(i))
jogada_willy = []
willy = input().split()
for j in willy:
    jogada_willy.append(int(j))


def contar_pontos(jp,jw):
    pontos_paes = 0
    pontos_willy = 0
    menor_paes = min(jogada_paes)
    maior_paes = max(jogada_paes)
    menor_willy = min(jogada_willy)
    maior_willy = max(jogada_willy)
    jogada_paes.sort()
    jogada_willy.sort()

    #analisando se todas são iguais
    if jogada_paes[0] == jogada_paes[1] == jogada_paes[2]:
        pontos_paes += menor_paes

    if jogada_willy[0] == jogada_willy[1] == jogada_willy[2]:
        pontos_willy += menor_willy

    #analisando cartas com soma igual 8
    if sum(jogada_paes) == 8:
        pontos_paes += 8

    if sum(jogada_willy) == 8:
        pontos_willy += 8

    #analisando se existem apenas duas menores cartas iguais
    if jogada_paes.count(menor_paes) == 2:
        pontos_paes += (menor_paes//2)
    if jogada_willy.count(menor_willy) == 2:
        pontos_willy += (menor_willy//2)

    #analisando se existem apenas duas maiores cartas iguais
    if jogada_paes.count(maior_paes) == 2:
        pontos_paes += (maior_paes//2)
    if jogada_willy.count(maior_willy) == 2:
        pontos_willy += (maior_willy//2)

   #analisando se estão em ordem crescente com distância 1

    if (jogada_paes[1] == (jogada_paes[0] + 1) == (jogada_paes[2]-1)):
        pontos_paes += menor_paes

    if (jogada_willy[1] == (jogada_willy[0] + 1) == (jogada_willy[2]-1)):
        pontos_willy += menor_willy
    
    
    if pontos_paes > pontos_willy:
        return 1
    elif pontos_willy > pontos_paes:
        return 2
    else:
        return 0

contar_pontos(jogada_paes,jogada_willy)
ganhador = contar_pontos(jogada_paes,jogada_willy)

if ganhador == 1:
    print(1)
elif ganhador == 2:
    print(2)
else:
    print(0)
