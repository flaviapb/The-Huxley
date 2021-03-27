notas = []
acima = 0
abaixo = 0
soma = 0
vezes = int(input())

for i in range(vezes):
    nota = float(input())
    notas.append(nota)
    soma += nota

for j in range(len(notas)):
    print("oi")
    


print(soma/len(notas))
print(acima)
print(abaixo)

