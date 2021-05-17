cont = 0
qntd_circulos = 0
maiorcirculo = 0
maiorlado = 0
multi = 0
while True:
    figura = input().lower()
    if figura == "sair":
        break
    else:
        if figura == "q":
            lado = int(input())
            if lado > maiorlado:
                maiorlado = lado
            cont += 1
        if figura == "r":
            base = int(input())
            altura = int(input())
            if (base * altura) > multi:
                multi = base * altura
            cont += 1
        if figura == "c":
            raio = int(input())
            if raio > maiorcirculo:
                maiorcirculo = raio
            cont += 1
            qntd_circulos += 1

def analisar_circulo(figura):
    if raio < 0:
        return -1
    else:
        return (maiorcirculo ** 2) * 3.14

def analisar_retangulo(figura):
    if base < 0 or altura < 0:
        return -1
    else:
        return (multi)

def analisar_quadrado(figura):
    if lado < 0:
        return -1
    else:
        return maiorlado ** 2

def printar():
    print("Maior circulo: {:.2f}".format(analisar_circulo(figura)))
    print("Maior retangulo: {:.2f}".format(analisar_retangulo(figura)))
    print("Maior quadrado: {:.2f}".format(analisar_quadrado(figura)))
    print("Quantidade de figuras {}".format(cont))
    print("Percentual de circulos: {:.2f}".format((qntd_circulos/cont)*100))

analisar_circulo(figura)
analisar_retangulo(figura)
analisar_quadrado(figura)
printar()