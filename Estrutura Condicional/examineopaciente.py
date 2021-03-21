"Desenvolvido por Flávia"


temp = float(input())
sintomas = input()

if sintomas != "S" and sintomas != "N":
  print("Erro")

elif temp >= 37 and sintomas == "S":
  print("Exames Especiais")

elif temp >= 37 and sintomas == "N":
  print("Exames Basicos")

elif temp < 37 and sintomas == "N":
  print("Liberado")

elif temp != 37 and sintomas == "S":
  print("Exames Basicos")