def calcular_digito(c):
    fatia_um = max(cpf[:4])
    fatia_dois = max(cpf[4:8])
    fatia_tres = max(cpf[8:11])
    fatia_quatro = cpf[12]
    soma = (int(fatia_um)+int(fatia_dois)+int(fatia_tres))
    divisao = soma%10
    
    if divisao == int(fatia_quatro):
        return "VALIDO"
    else:
        return "INVALIDO"
            
                    
while True:
    cpf = input().upper()
    if cpf == "FIM":
        break
    else:
        print(calcular_digito(cpf)) #pode ser assim
        #ou assim
        printar = calcular_digito(cpf)
        if printar == "VALIDO":
            print("VALIDO")
        else:
            print("INVALIDO")