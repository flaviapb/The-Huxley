"Desenvolvido por Flávia"

idade = int(input())
tipo = input()

if (idade < 0) or (idade > 130):
  print ("Idade invalida.")

elif (tipo != "azar") and (tipo != "mmorpg") and (tipo != "moba") and (tipo != "casual"):
  print ("Jogo invalido.")

elif (tipo == "azar" and idade >= 21) or (tipo == "mmorpg" and idade >= 14) or (tipo == "moba" and idade >= 10) or (tipo == "casual"):
  print("Pode entrar!")

elif (tipo == "azar" and idade < 21) or (tipo == "mmorpg" and idade < 14) or (tipo == "moba" and idade < 10):
  print("Volte daqui h� alguns anos.")