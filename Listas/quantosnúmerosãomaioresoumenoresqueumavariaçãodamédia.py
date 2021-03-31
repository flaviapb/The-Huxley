notas = []
acima = 0
abaixo = 0
soma = 0
vezes = int(input())

for i in range(vezes):
    nota = float(input())
    notas.append(nota)
    soma += nota


media = soma/len(notas)

for i in range(vezes):
    if notas[i] >= media + (media * 0.1):
        acima += 1
    if notas[i] < media - (media * 0.1): 
        abaixo += 1

   
print("{:.2f}".format(media))
print(acima)
print(abaixo)