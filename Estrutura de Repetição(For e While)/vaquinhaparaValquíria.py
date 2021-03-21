"Desenvolvido por Flávia"

cont = 0
media = 0
print("Insira os valores das doacoes:")
valor = []

num = float(input())
if num < 0:
  print("Total arrecadado: 0.00")
  print("Valor medio da doacao: 0.00")

else:
  while num > 0:
    valor.append(num)
    soma = sum(valor)
    media += 1
    num = float(input())

  print("Total arrecadado: {:.2f}".format(soma))
  print("Valor medio da doacao: {:.2f}".format(soma/media))