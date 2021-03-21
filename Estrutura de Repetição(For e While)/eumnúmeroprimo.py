"Desenvolvido por Flávia"

num = int(input())

while num != -1:

  if num == -1:
    break
    
  else:
    vezes = 0
    for i in range(1, num+1):
      if num % i == 0:
        vezes += 1
      
    if vezes == 2:
      print("1")
      
    else:
      print("0")

    num = int(input())