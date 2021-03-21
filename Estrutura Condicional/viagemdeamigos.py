"Desenvolvido por Flávia"

qntd_pessoas = int(input())
cidade = input().upper()
qntd_quartos = int(input())

if (cidade == "PIPA") and (qntd_quartos == 2 ):
  total_viajem = (600 + (75 * qntd_pessoas))
  total_pessoa = total_viajem / qntd_pessoas
  print("{:.2f}".format(total_viajem))
  print("{:.2f}".format(total_pessoa))

elif (cidade == "PIPA") and (qntd_quartos == 3 ):
  total_viajem = (900 + (75 * qntd_pessoas))
  total_pessoa = total_viajem / qntd_pessoas
  print("{:.2f}".format(total_viajem))
  print("{:.2f}".format(total_pessoa))

elif (cidade == "FORTALEZA") and (qntd_quartos == 3 ):
  total_viajem = (950 + (60 * qntd_pessoas))
  total_pessoa = total_viajem / qntd_pessoas
  print("{:.2f}".format(total_viajem))
  print("{:.2f}".format(total_pessoa))

elif (cidade == "FORTALEZA") and (qntd_quartos == 4 ):
  total_viajem = (1120 + (60 * qntd_pessoas))
  total_pessoa = total_viajem / qntd_pessoas
  print("{:.2f}".format(total_viajem))
  print("{:.2f}".format(total_pessoa))