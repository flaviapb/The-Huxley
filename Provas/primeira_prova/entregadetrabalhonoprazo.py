                                          "Desenvolvido por Flávia"

dia = int(input())
dia_apresentacao = int(input())

if dia > dia_apresentacao:
  print("Eu odeio a professora!")

elif dia < (dia_apresentacao -3 ):
  print("Muito bem! No prazo!")

elif dia == dia_apresentacao:
  print("Parece o trabalho do meu filho!")
  print("Voce falhou! Ate a proxima!")
  
elif dia <= (dia_apresentacao -1 ):
  print("Parece o trabalho do meu filho!")
  if dia_apresentacao < 24:
    print("Trabalho Apresentado!")
  else:
    print("Voce falhou! Ate a proxima!")