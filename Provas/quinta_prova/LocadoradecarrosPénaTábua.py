def validar_datas(qi):
    if int(qi[1]) == 2:
        if int(qi[0])>= 1 and int(qi[0]) > 28:
            return "Data invalida"
    if int(qi[0]) > 30:
        return "Data invalida"

def validar_devolucao(qi,qf):
    if (qi[0] > qf[0] and qi[1] == qf[1]) or (qi[1]>qf[1]) or (qi[2] > qf[2]):
        return "Data de devolucao inferior a data de locacao"
    else:
        if int(qi[1]) == int(qf[1]) and int(qi[2]) == int(qf[2]) and int(qi[0]) <= int(qf[0]):
            return ((int(qi[0])) + int(30) + (int(qi[2])*360)) - ((int(qf[0])) + (int(30)) + (int(qf[2])*360))

        if qi[1] == "02" or qf[1] == "02":
            return ((int(qi[0])) + int(28) + (int(qi[2])*360)) - ((int(qf[0])) + (int(30)) + (int(qf[2])*360))

        elif  int(qi[2]) == int(qf[2]) and int(qi[1]) <= int(qf[1]):
            return ((int(qi[0])) + int(30) + (int(qi[2])*360)) - ((int(qf[0])) + (int(30)) + (int(qf[2])*360))

        elif int(qi[2]) < int(qf[2]):
            return ((int(qi[0])) + int(30) + (int(qi[2])*360)) - ((int(qf[0])) + (int(30)) + (int(qf[2])*360))

def validar_carro(m):
    excessao = ["B","I","P"]
    if modelo not in excessao:
        return "Modelo de carro invalido"

def validar_quilometragem(quilo):
    if int(quilo[0]) < int(quilo[1]):
        return (int(quilo[1]) - int(quilo[0])) * 0.30
    else:
        return "Valores do odometro com erro"

while True:
    modelo = input().upper()
    if modelo == "FIM":
        break
    qntd_aluguel_inicial = input().split("/")
    qntd_aluguel_final = input().split("/")
    quilometragem = input().split(" ")
    #datas certas
    validacao1 = validar_datas(qntd_aluguel_inicial)
    validacao2 = validar_datas(qntd_aluguel_final)
    if validacao1 == "Data invalida" or validacao2 == "Data invalida":
        print("Data invalida")
    else:
        #contagem de dias da devolução
        diaria = validar_devolucao(qntd_aluguel_inicial,qntd_aluguel_final)
        if diaria == "Data de devolucao inferior a data de locacao":
            print("Data de devolucao inferior a data de locacao")
        else:
            #sobre os modelos
            valor_carro = validar_carro(modelo)
            if valor_carro == "Modelo de carro invalido":
                print(validar_carro(modelo))
            else:
                valor = 0
                if modelo == "B":
                    valor += 30
                if modelo == "I":
                    valor += 40
                if modelo == "P":
                    valor += 60
                #sobre os km
                quilometros = validar_quilometragem(quilometragem)
                if quilometros == "Valores do odometro com erro":
                    print("Valores do odometro com erro")
                else:
                    def aluguel(valor,diaria,quilometros):
                        valordalocacao = -1 * (valor * diaria) + quilometros
                        return valordalocacao 

                    print("{:.2f}".format(aluguel(valor,diaria,quilometros)))