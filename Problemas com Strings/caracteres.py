"Desenvolvido por Flávinha"

palavras = []
while True:
    tamanho = int(input())
    if tamanho == 0:
        break
    else:
        palavra = input()
        palavras.append(palavra)

for i in range(len(palavras)): 
    print(palavras[i][::-1])