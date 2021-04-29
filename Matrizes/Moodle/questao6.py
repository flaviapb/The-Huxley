matriz = []
soma1 = 0
soma2 = 0
soma3 = 0
soma4 = 0
somageral= []

for i in range(3):
    linha = []
    for j in range(4):
        elemento = int(input())
        linha.append(elemento)
    matriz.append(linha)

print("\n")
for i in matriz:
    print(*i)
print("\n")
for n in matriz:
    soma1 += n[0]
    soma2 += n[1]
    soma3 += n[2]
    soma4 += n[3]

print("[{}] [{}] [{}] [{}]".format(soma1,soma2,soma3,soma4))
    