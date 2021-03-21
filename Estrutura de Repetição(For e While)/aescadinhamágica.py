"Desenvolvido por Flávia"

num = int(input())
for valor in range(1,num+1):              
  for i in range(1,valor+1):
    if i == valor:
      print(i)
    else:
      print(i,end=' ')