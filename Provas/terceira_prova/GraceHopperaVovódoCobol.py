                                                    "Desenvolvido por Flávia"      

while True:
    texto = str(input().upper())
    if texto == "FIM":
        break
    palavra = texto.split("-")
    cobol = ""
    for l in palavra:
        if len(cobol) == 0 and (l[0] == "C" or l[-1] == "C"):
            cobol += "C"
        elif len(cobol) == 1 and (l[0] == "O" or l[-1] == "O"):
            cobol += "O"
        elif len(cobol) == 2 and (l[0] == "B" or l[-1] == "B"):
            cobol += "B"
        elif len(cobol) == 3 and (l[0] == "O" or l[-1] == "O"):
            cobol += "O"
        elif len(cobol) == 4 and (l[0] == "L" or l[-1] == "L"):
            cobol += "L"
            

    if cobol == "COBOL":
        print('GRACE HOPPER')
    else:
        print('BUG')