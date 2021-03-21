"Desenvolvido por Flávia"

nome = input()
salario_fixo = float(input())
vendas_total = float(input())
total_mes = salario_fixo + (vendas_total * 0.15)
print("TOTAL = R$ {:.2f}".format(total_mes))