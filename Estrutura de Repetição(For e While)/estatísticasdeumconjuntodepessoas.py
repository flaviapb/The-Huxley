"Desenvolvido por Flávia"

qntd_homem = 0
qntd_mulher = 0
qntd_sexos_ambos = 0
salarios = 0
salario_mulher = 0
salario_homem = 0
maior_salario_mulher = 0
maior_salario_homem = 0
qntd_sexos_ambos = 0
soma_salario_homem = 0

for i in range(10):
    salario = float(input())
    salarios += salario
    sexo = input().lower()
    qntd_sexos_ambos += 1
    media_salario = salarios/qntd_sexos_ambos

    if sexo == "f": 
        qntd_mulher += 1
        salario_mulher = salario
        if salario > maior_salario_mulher:
            maior_salario_mulher = salario
    if sexo == "m":
        qntd_homem += 1
        salario_homem += salario
        if salario > maior_salario_homem:
            maior_salario_homem = salario
        media_homem = salario_homem/qntd_homem


print(qntd_homem)
print(qntd_mulher)
print("{:.1f}".format(media_salario))
if maior_salario_mulher > maior_salario_homem:
  print("f")
else:
  print("m")

print("{:.1f}".format(media_homem))