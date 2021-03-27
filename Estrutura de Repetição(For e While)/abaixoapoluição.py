"Desenvolvido por Flávia Renata"

multas = []
cont = 0 

while cont <= 0:
  qntd_carro = int(input())
  if qntd_carro == 999:
    break
    cont += 1
  else:
    if qntd_carro != 999:
      if qntd_carro > 2:
        extra = qntd_carro - 2
        multas.append(extra)

print("{:.2f}".format(sum(multas)*12.89))
print(len(multas))