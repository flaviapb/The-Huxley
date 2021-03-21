"Desenvolvido por Flávia"

num1=int(input())
num2=int(input())

if num1 <= num2:
  menor = num1
  maior = num2
else:
  menor = num2
  maior = num1
cont = 0
for i in range(menor,maior+1):
  if  i > 0:
    cont += i

print(cont)