dia = int(input())
mes = int(input())

def EstacaoAno(dia,mes):
    if mes == 1 or mes == 2:
        return "VERAO"
    elif mes == 3:
        if dia <= 20:
            return "VERAO"
        else:
            return "OUTONO"

    if mes == 4 or mes == 5:
        return "OUTONO"
    elif mes == 6:
        if dia <= 20:
            return "OUTONO"
        else:
            return "INVERNO"
    
    if mes == 7 or mes == 8:
        return "INVERNO"
    elif mes == 9:
        if dia <= 20:
            return "INVERNO"
        else:
            return "PRIMAVERA"

    if mes == 10 or mes == 11:
        return "PRIMAVERA"
    elif mes == 12:
        if dia <= 20:
            return "PRIMAVERA"
        else:
            return "VERAO"

printar = EstacaoAno(dia,mes)

if printar == "VERAO":
    print("VERAO")
elif printar == "PRIMAVERA":
    print("PRIMAVERA")
elif printar == "OUTONO":
    print("OUTONO")
elif printar == "INVERNO":
    print("INVERNO")

"""Primavera: 21 setembro até 20 dezembro  
Verão: 21 dezembro até 20 março   
Outono: 21 março até 20 junho
Inverno: 21 junho até 20 setembro"""

