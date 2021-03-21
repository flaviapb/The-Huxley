"Desenvolvido por Flávia"

qntd_sexo = 0
aprovados = 0
qntd_mulher = 0
qntd_homem = 0

while True:
  nota = int(input())
  if nota < 0:
    break
  else:
    while nota > 100:
      print("Digite uma nota inferior a 100.")
      nota = int(input())
    else:
      redacao = int(input())
      while redacao > 100:
        print("Digite uma nota inferior a 100.")
        redacao = int(input()) 
      else:
        sexo = input().upper()
        qntd_sexo += 1
        if sexo == "F" and ((nota + redacao)/2 >= 60) and nota > 40 and redacao > 40:
          qntd_mulher += 1
        if sexo == "M" and ((nota + redacao)/2 >= 60) and nota > 40 and redacao > 40:
          qntd_homem += 1
  
    if ((nota + redacao)/2 >= 60) and nota > 40 and redacao > 40:
      aprovados += 1
  


print("{} candidato(s) inscrito(s).".format(qntd_sexo))
print("{} candidato(s) aprovado(s).".format(aprovados))
print("{} mulher(es) e {} homem(ns).".format(qntd_mulher,qntd_homem))