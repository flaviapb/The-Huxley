"Desenvolvido por Flávia"


qntd_portugues = int(input())
aprovados = 0

while qntd_portugues > 0:
  qntd_matematica = int(input())
  nota_redacao = float(input())
  
  if qntd_portugues < 0:
    break
 
  else:
    if qntd_portugues >= 40 and qntd_matematica >= 21 and nota_redacao >= 7.0:
      aprovados += 1

    qntd_portugues = int(input())
  
print(aprovados)