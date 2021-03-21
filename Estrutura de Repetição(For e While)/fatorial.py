"Desenvolvido por Flávia"

while True:
  num = int(input())
  if num == -1:
    break
  else:
    total = 1
    for n in range(num):
      total = total * (n + 1)
  print(total)