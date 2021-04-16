                                        "Desenvolvido por Flávia"

idade = int(input("Sua idade:\n"))
profissao = int(input("Profissao(1-saude;2-indigenas;3-professores;4-seguranca;5-sistema prisional; 6-outro):\n"))
cormobidades = input("Tem comorbidades (s/n)?\n")
res_institucionalizada = input("Mora em residencia institucionalizada(s/n)?\n")
print("--------------------------")


if profissao >= 7:
  print("Voce informou um codigo de profissao invalido")

elif profissao == 1:
  print("Voce eh do grupo 1 e serah vacinado na Fase 1")

elif profissao == 2 or (idade >= 60 and res_institucionalizada == "s"):
  print("Voce eh do grupo 2 e serah vacinado na Fase 1")

elif (idade >= 75 and idade <= 79) or idade >= 80:
  print("Voce eh do grupo 2 e serah vacinado na Fase 1")

elif (idade >= 70 and idade <= 74):
  print("Voce eh do grupo 3 e serah vacinado na Fase 2")

elif (idade >= 65 and idade <= 69):
  print("Voce eh do grupo 4 e serah vacinado na Fase 2")

elif (idade >= 60 and idade <= 64):
  print("Voce eh do grupo 5 e serah vacinado na Fase 2")

elif cormobidades == "s":
  print("Voce eh do grupo 6 e serah vacinado na Fase 3")

elif profissao == 3:
  print("Voce eh do grupo 7 e serah vacinado na Fase 4")

if profissao == 4 or profissao == 5:
  print("Voce eh do grupo 8 e serah vacinado na Fase 4")