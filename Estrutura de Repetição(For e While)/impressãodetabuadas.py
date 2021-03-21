"Desenvolvido por Flávia"


while True:
  num1 = int(input())
  if (num1 < 1 or num1 > 9):
    print("Insira um n�mero inicial entre 1 e 9")
  else:
    break

while True:
  num2 = int(input())
  if (num2 < 1 or num2 > 9):
    print("Insira um n�mero final entre 1 e 9")
  else:
    break


if num1 > num2:
  print("Nenhuma tabuada nesse intervalo")


for i in range (num1, num2+1):
    for j in range(1, 10):
        print(i, "x", j, "=", i*j)
    print()