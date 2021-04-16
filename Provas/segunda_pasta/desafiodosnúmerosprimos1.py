                                                "Desenvolvido por Flávia"


while True:
  num = int(input())
  if num >= 2 and num <= 12:
    break
  else:
    print("Informe um valor entre 2 e 12!") 

cont = 0
while True:
  qntd_primos = 2
  valor = int(input())
  for i in range(2, valor+1):
    if valor % qntd_primos == 0 and valor != qntd_primos:
      continue
    elif valor == qntd_primos:
      print(valor, end=" ")
      cont += 1
      break
    else:
      qntd_primos += 1

  if cont == num:
    break