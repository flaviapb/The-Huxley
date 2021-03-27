notas = []
soma = 0


while True:
    vezes = int(input())
    if vezes <= 0 or vezes > 5:
        print("Numero de notas invalido.")
        break
    
    else:
        for i in range(vezes):
            nota = float(input())
            notas.append(nota)
            soma += nota
            print("Nota {}: {}".format(i+1,nota))


    print("Media: {:.2f}".format(soma/len(notas)))
    break

