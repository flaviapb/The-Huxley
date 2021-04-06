maior = "" #deixando vazia
while True:
    frase = input().split() 
    tamanho = []
    if frase == ['0']:
        break
    for i in frase:
        tamanho.append(str(len(i)))
        for i in range(len(tamanho)):
            if len(frase[i]) >= len(maior):
                maior = frase[i]
    num = "-".join(tamanho)
    print(num)
print("Maior palavra: ",maior)