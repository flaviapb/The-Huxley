"Desenvolvido por Flávia"

escala = input()
temperatura = float(input())

if escala == "C" and temperatura <= -273.0:
  print("Valor de temperatura abaixo do minimo")

if escala == "C" and temperatura > -273.0:
  nova_temp_1 = (temperatura * 9/5) + 32
  print("{:.2f} F".format(nova_temp_1))
  nova_temp_2 = temperatura + 273.15
  print("{:.2f} K".format(nova_temp_2))

if escala == "F" and temperatura <= -459.67:
  print("Valor de temperatura abaixo do minimo")

if escala == "F" and temperatura > -459.67:
  nova_temp_3 = (temperatura - 32) * 5/9
  print("{:.2f} C".format(nova_temp_3))
  nova_temp_4 = (temperatura - 32) * 5/9 + 273.15 
  print("{:.2f} K".format(nova_temp_4))

if escala == "K" and temperatura <= -0.0:
    print("Valor de temperatura abaixo do minimo")

if escala == "K" and temperatura > -0.0:
  nova_temp_5 = temperatura - 273.15  
  print("{:.2f} C".format(nova_temp_5))
  nova_temp_6 = (temperatura - 273.15) * 9/5 + 32 
  print("{:.2f} F".format(nova_temp_6))