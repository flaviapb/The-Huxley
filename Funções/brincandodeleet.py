frase = input()

def analisar_erros(frase):
    num = "0","1","2","3","4","5","6","7","8","9"
    for i in frase:
        if i in num:
            print("numeros")
            print("0")
            return 0
    if frase == "":
        print("Estamos com problemas na conexão com o servidor")
        return 0
    return 1

analisar = analisar_erros(frase)
if analisar == 0:
    exit()
else:
    def codificar(frase):
        cont = 0
        codigo = ""
        for i in frase[::-1]:
            if i == "a" or i == "A":
                codigo += "@"
                cont += 1
            elif i == "e" or i == "E":
                codigo += "3"
                cont += 1
            elif i == "i" or i == "I":
                codigo += "1"
                cont += 1
            elif i == "o" or i == "O":
                codigo += "0"
                cont += 1
            elif i == "t" or i == "T":
                codigo += "7"
                cont += 1
            elif i == "s" or i == "S":
                codigo += "5"
                cont += 1
            else:
                codigo += i
        print(codigo)
        print(cont)


def printar(frase):
    codificar(frase)

analisar_erros(frase)
printar(frase)