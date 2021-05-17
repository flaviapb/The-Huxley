media = float(input())
faltas = int(input())

def ClassificaAluno(m,f):
    if (media >= 7 and media < 9.5) and faltas <=10:
        return "APROVADO"
    elif faltas > 10:
        return "REPROVADO POR FALTAS"
    elif ( media >= 9.5) and faltas < 10:
        return "APROVADO COM LOUVOR"
    else:
        return "REPROVADO"

ClassificaAluno(media,faltas)

printar = ClassificaAluno(media,faltas)

if printar == "APROVADO":
    print("APROVADO")
elif printar == "REPROVADO POR FALTAS":
    print("REPROVADO POR FALTAS")
elif printar == "APROVADO COM LOUVOR":
    print("APROVADO COM LOUVOR")
else:
    print("REPROVADO")

