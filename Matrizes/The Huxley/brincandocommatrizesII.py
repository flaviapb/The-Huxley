matriz = []
soma = []
for l in range(3):
    linha = []
    for c in range(3):
        elemento = int(input())
        if elemento > 0:
            soma.append(elemento)
        linha.append(elemento)
    matriz.append(linha)

media = sum(soma)/len(soma) #media

menorvalor = matriz [0][0] #menorvalor (início)
for i in matriz:
    if menorvalor > min(i):
        menorvalor = min(i)  #menorvalor (final)

delta = " "   #delta (início)
if menorvalor % 2 == 0:
    delta = 1
else:
    delta = 0 #delta (final)

 
del matriz[0][0]  #deletando diagonal principal
del matriz[1][1]  #deletando diagonal principal
del matriz[2][2]  #deletando diagonal principal

soma = 0 #Somando sem a diagonal principal
for i in matriz:
    soma += sum(i) #acaba aqui

print("{:.2f} {} {} {}".format(media,menorvalor,delta,soma)) #printando na mesma linha