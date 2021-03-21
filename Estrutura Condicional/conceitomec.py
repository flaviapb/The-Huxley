"Desenvolvido por Flávia"

qntd_livros = int(input())
qntd_alunos = int(input())
media = qntd_alunos / qntd_livros

if media >= 1 and media <= 8:
  print("A")

elif media >= 1 and (media >= 9 and media <= 12):
  print("B")

elif media >= 1 and (media >= 13 and media <= 18):
  print("C")
  
elif  media > 18:
  print("D")