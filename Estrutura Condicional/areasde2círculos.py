"Desenvolvido por Flávia"

circulo_1 = float(input()) 
circulo_2 = float(input()) 
pi = 3.14
raio_1 = float(pi * (circulo_1 ** 2))
raio_2 = float(pi * (circulo_2 ** 2))

if circulo_1 > circulo_2:
    print("Primeiro circulo")

elif circulo_1 < circulo_2: 
    print("Segundo circulo")

elif circulo_1 == circulo_2:
    print("Iguais")
