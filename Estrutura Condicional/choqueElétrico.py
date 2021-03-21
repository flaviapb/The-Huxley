"Desenvolvido por Flávia"

level = int(input())

if level >= 1 and level <= 20: 
  p1 = 20 + (level ** 3)
  print("Potencia de : {} W".format(p1))

if level >= 21 and level <= 40: 
  p2 = 8000 + ((level - 10)**2)
  print("Potencia de : {} W".format(p2))  

elif  level >= 41 and level <= 60 : 
  p3 = 9000 + (level * 5)
  print("Potencia de : {} W".format(p3))

elif level >= 61 and level <= 80: 
  p4 = 9300 + (level * 2)
  print("Potencia de : {} W".format(p4))

elif level >= 81 and level <= 100: 
  p5 = 9500 + level 
  print("Potencia de : {} W".format(p5))