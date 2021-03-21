"Desenvolvido por Flávia"

dia = input()
preco = float(input())
op_produto = input()
nome_produto = input()

if (dia == "seg" or dia == "ter" or dia == "qua") and op_produto == "ouro":
  preco_novo = preco / 2 
  print("O preco do produto {} no dia {} eh {:.2f}".format(nome_produto, dia, preco_novo))

elif (dia == "qui" or dia == "sex") and (preco >= 10 and preco <= 100.00 ):
  preco_novo = preco / 3
  print("O preco do produto {} no dia {} eh {:.2f}".format(nome_produto, dia, preco_novo))

elif (dia == "sab") and (op_produto == "prata"):
  preco_novo = preco * 3 
  print("O preco do produto {} no dia {} eh {:.2f}".format(nome_produto, dia, preco_novo))

else: 
  preco_novo = preco * 2 
  print("O preco do produto {} no dia {} eh {:.2f}".format(nome_produto, dia, preco_novo))