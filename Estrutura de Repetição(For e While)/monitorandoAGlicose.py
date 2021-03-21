"Desenvolvido por Flávia"


num = int(input())
valor = 0
total = 0

while num != 0:
  valor += num
  total += 1
  num = int(input())
  
if valor/total < 110:
  print("Glicose Normal")
  
elif valor/total >= 200:
  print("Glicose Muito Alta")
  
else:
  print("Glicose Alterada")