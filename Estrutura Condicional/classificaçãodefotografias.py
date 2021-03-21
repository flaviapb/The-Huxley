"Desenvolvido por Flávia"

psrn = int(input())
enqua = input()
expo = input()

if (psrn >= 80 and psrn <= 90) and (enqua == "bom" or enqua == "excelente") and (expo == "bem exposta"):
  print("para imprimir")

elif (psrn >= 80 and psrn <= 90) and (enqua == "bom" or enqua == "excelente") and (expo == "subexposta" or expo == "superexposta"):
  print("boa")

elif (psrn >= 80 and psrn <= 90) and (enqua == "ruim") and (expo == "subexposta" or expo == "superexposta" or expo == "bem exposta"):
  print("marromeno")

elif (psrn >= 50 and psrn <= 80) and (enqua == "excelente") and (expo == "bem exposta"):
  print("boa")

elif (psrn >= 50 and psrn <= 80) and (enqua == "ruim" or enqua == "bom") and (expo == "subexposta" or expo == "superexposta" or expo == "bem exposta"):
  print("marromeno")

elif (psrn < 50 ) and (enqua == "excelente") and (expo == "bem exposta"):
  print("marromeno")

elif (psrn < 50) and (enqua == "ruim" or enqua == "bom" or enqua == "excelente") and (expo == "subexposta" or expo == "superexposta" or expo == "bem exposta"):
  print("lixo")