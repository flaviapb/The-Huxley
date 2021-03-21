"Desenvolvido por Flávia"

altura = float(input())
raio = float(input())
pi = 3.14
volume = pi * (raio ** 2) * altura
area = (2 * pi * raio) * (raio + altura)
print("{:.2f}".format(volume))
print("{:.2f}".format(area))