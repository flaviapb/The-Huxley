"Desenvolvido por Flávia"

nome = input()
if nome != "Homem de Ferro" and nome != "Hulk" and nome != "Capit�o Am�rica" and nome != "Thor" and nome != "Gavi�o Arqueiro" and nome != "Vi�va Negra":
  print("Vingador Inv�lido")

else:
  poder = input()
  energia = int(input())
#condi��es sobre conseguir derrotar Thanos
  if (nome == "Homem de Ferro") and (poder == "Armadura de Ferro") and (energia >= 10):
    print("{} conseguiu derrotar Thanos".format(nome))
  elif (nome == "Hulk") and (poder == "For�a Bruta") and (energia >= 5):
    print("{} conseguiu derrotar Thanos".format(nome))
  elif (nome == "Capit�o Am�rica") and (poder == "Escudo") and (energia >= 7):
    print("{} conseguiu derrotar Thanos".format(nome))
  elif (nome == "Thor") and (poder == "Martelo") and (energia >= 4):
    print("{} conseguiu derrotar Thanos".format(nome))
  elif (nome == "Gavi�o Arqueiro") and (poder == "Arco e Flecha") and (energia >= 12):
    print("{} conseguiu derrotar Thanos".format(nome))
  elif (nome == "Vi�va Negra") and (poder == "Intelig�ncia") and (energia >= 20):
    print("{} conseguiu derrotar Thanos".format(nome))
  
  #condi��es sobre n�o conseguir derrotar Thanos
  if (nome == "Homem de Ferro") and (poder == "Armadura de Ferro") and (energia < 10):
    print("{} NAO conseguiu derrotar Thanos, chamem outro Vingador".format(nome))
  elif (nome == "Hulk") and (poder == "For�a Bruta") and (energia < 5):
    print("{} NAO conseguiu derrotar Thanos, chamem outro Vingador".format(nome))
  elif (nome == "Capit�o Am�rica") and (poder == "Escudo") and (energia < 7):
    print("{} NAO conseguiu derrotar Thanos, chamem outro Vingador".format(nome))
  elif (nome == "Thor") and (poder == "Martelo") and (energia >= 4):
    print("{} NAO conseguiu derrotar Thanos, chamem outro Vingador".format(nome))
  elif (nome == "Gavi�o Arqueiro") and (poder == "Arco e Flecha") and (energia < 12):
    print("{} NAO conseguiu derrotar Thanos, chamem outro Vingador".format(nome))
  elif (nome == "Vi�va Negra") and (poder == "Intelig�ncia") and (energia < 20):
    print("{} NAO conseguiu derrotar Thanos, chamem outro Vingador".format(nome))

  #Condi��es sobre n�o ser o Homem de Ferro
  if (nome == "Homem de Ferro") and (poder == "For�a Bruta") and (energia <= 10):
    print("{} NAO conseguiu derrotar Thanos".format(nome))
    print("Esse � o poder do Hulk")
  elif nome == ("Homem de Ferro") and (poder == "Escudo") and (energia <= 10):
    print("{} NAO conseguiu derrotar Thanos".format(nome))
    print("Esse � o poder do Capit�o Am�rica")
  elif nome == ("Homem de Ferro") and (poder == "Martelo") and (energia <= 10):
    print("{} NAO conseguiu derrotar Thanos".format(nome))
    print("Esse � o poder do Thor")
  elif nome == ("Homem de Ferro") and (poder == "Arco e Flecha") and (energia <= 10):
    print("{} NAO conseguiu derrotar Thanos".format(nome))
    print("Esse � o poder do Gavi�o Arqueiro")
  elif nome == ("Homem de Ferro") and (poder == "Intelig�ncia") and (energia <= 10):
    print("{} NAO conseguiu derrotar Thanos".format(nome))
    print("Esse � o poder da Vi�va Negra")

  #Condi��es sobre n�o ser o Hulk 
  elif (nome == "Hulk") and (poder == "Escudo") and (energia <= 5):
    print("{} NAO conseguiu derrotar Thanos".format(nome))
    print("Esse � o poder do Capit�o Am�rica")
  elif (nome == "Hulk") and (poder == "Intelig�ncia") and (energia <= 5):
    print("{} NAO conseguiu derrotar Thanos".format(nome))
    print("Esse � o poder da Vi�va Negra")
  elif (nome == "Hulk") and (poder == "Arco e Flecha") and (energia <= 5):
    print("{} NAO conseguiu derrotar Thanos".format(nome))
    print("Esse � o poder do Gavi�o Arqueiro")
  elif (nome == "Hulk") and (poder == "Martelo") and (energia <= 5):
    print("{} NAO conseguiu derrotar Thanos".format(nome))
    print("Esse � o poder do Thor")
  elif (nome == "Hulk") and (poder == "Armadura de Ferro") and (energia <= 5):
    print("{} NAO conseguiu derrotar Thanos".format(nome))
    print("Esse � o poder do Homem de Ferro")

  #Condi��es sobre n�o ser o capit�o america
  elif (nome == "Capit�o Am�rica") and (poder == "Intelig�ncia") and (energia <= 7):
    print("{} NAO conseguiu derrotar Thanos".format(nome))
    print("Esse � o poder da Vi�va Negra")
  elif (nome == "Capit�o Am�rica") and (poder == "Martelo") and (energia <= 7):
    print("{} NAO conseguiu derrotar Thanos".format(nome))
    print("Esse � o poder do Thor")
  elif (nome == "Capit�o Am�rica") and (poder == "Arco e Flecha") and (energia <= 7):
    print("{} NAO conseguiu derrotar Thanos".format(nome))
    print("Esse � o poder do Gavi�o Arqueiro")
  elif (nome == "Capit�o Am�rica") and (poder == "Armadura de Ferro") and (energia <= 7):
    print("{} NAO conseguiu derrotar Thanos".format(nome))
    print("Esse � o poder do Homem de Ferro")
  elif (nome == "Capit�o Am�rica") and (poder == "For�a Bruta") and (energia <= 7):
    print("{} NAO conseguiu derrotar Thanos".format(nome))
    print("Esse � o poder do Hulk")

  #Condi��es sobre n�o ser o Thor
  elif (nome == "Thor") and (poder == "Intelig�ncia") and (energia <= 4):
    print("{} NAO conseguiu derrotar Thanos".format(nome))
    print("Esse � o poder da Vi�va Negra")
  elif (nome == "Thor") and (poder == "For�a Bruta") and (energia <= 4):
    print("{} NAO conseguiu derrotar Thanos".format(nome))
    print("Esse � o poder do Hulk")
  elif (nome == "Thor") and (poder == "Armadura de Ferro") and (energia <= 4):
    print("{} NAO conseguiu derrotar Thanos".format(nome))
    print("Esse � o poder do Homem de Ferro")
  elif (nome == "Thor") and (poder == "Arco e Flecha") and (energia <= 4):
    print("{} NAO conseguiu derrotar Thanos".format(nome))
    print("Esse � o poder do Gavi�o Arqueiro")
  elif (nome == "Thor") and (poder == "Escudo") and (energia <= 4):
    print("{} NAO conseguiu derrotar Thanos".format(nome))
    print("Esse � o poder do Capit�o Am�rica")

  #Condi��es sobre n�o ser o Gavi�o Arqueiro
  elif (nome == "Gavi�o Arqueiro") and (poder == "Escudo") and (energia <= 12):
    print("{} NAO conseguiu derrotar Thanos".format(nome))
    print("Esse � o poder do Capit�o Am�rica")
  elif (nome == "Gavi�o Arqueiro") and (poder == "Armadura de Ferro") and (energia <= 12):
    print("{} NAO conseguiu derrotar Thanos".format(nome))
    print("Esse � o poder do Homem de Ferro")
  elif (nome == "Gavi�o Arqueiro") and (poder == "Intelig�ncia") and (energia <= 12):
    print("{} NAO conseguiu derrotar Thanos".format(nome))
    print("Esse � o poder da Vi�va Negra")
  elif (nome == "Gavi�o Arqueiro") and (poder == "For�a Bruta") and (energia <= 12):
    print("{} NAO conseguiu derrotar Thanos".format(nome))
    print("Esse � o poder do Hulk")
  elif (nome == "Gavi�o Arqueiro") and (poder == "Martelo") and (energia <= 12):
    print("{} NAO conseguiu derrotar Thanos".format(nome))
    print("Esse � o poder do Thor")
  
  #Condi��es sobre n�o ser a Vi�va Negra
  elif (nome == "Vi�va Negra") and (poder == "Martelo") and (energia <= 20):
    print("{} NAO conseguiu derrotar Thanos".format(nome))
    print("Esse � o poder do Thor")
  elif (nome == "Vi�va Negra") and (poder == "For�a Bruta") and (energia <= 20):
    print("{} NAO conseguiu derrotar Thanos".format(nome))
    print("Esse � o poder do Hulk")
  elif (nome == "Vi�va Negra") and (poder == "Armadura de Ferro") and (energia <= 20):
    print("{} NAO conseguiu derrotar Thanos".format(nome))
    print("Esse � o poder do Homem de Ferro")
  elif (nome == "Vi�va Negra") and (poder == "Escudo") and (energia <= 20):
    print("{} NAO conseguiu derrotar Thanos".format(nome))
    print("Esse � o poder do Capit�o Am�rica")
  elif (nome == "Vi�va Negra") and (poder == "Arco e Flecha") and (energia <= 20):
    print("{} NAO conseguiu derrotar Thanos".format(nome))
    print("Esse � o poder do Gavi�o Arqueiro")