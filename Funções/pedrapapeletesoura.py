def jogo_pedra_papel_tesoura():
    for i in range(5):
        op1 = input().upper()
        op2 = input().upper()

    jogador1 = 0
    jogador2 = 0
    for i in range(5):
                        #Jogador1 = Maria
        if op1 == "TESOURA" and op2 == "PAPEL":
            jogador1 += 1
        
        elif op1 == "PAPEL" and op2 == "PEDRA":
            jogador1 += 1
        
        elif op1 == "PEDRA" and op2 == "TESOURA":
            jogador1 += 1

                        #Jogador2 = Miguel
        
        if op2 == "TESOURA" and op1 == "PAPEL":
            jogador2 += 1
        
        elif op2 == "PAPEL" and op1 == "PEDRA":
            jogador2 += 1
        
        elif op2 == "PEDRA" and op2 == "TESOURA":
            jogador2 += 1

    if jogador2 > jogador1:
        print("MIGUEL")
    elif jogador1 > jogador2:
        print("MARIA")

jogo_pedra_papel_tesoura()