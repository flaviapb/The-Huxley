vezes = int(input())
qntd_latas_copos = []
cont = 0

for i in range(vezes):
    for j in range(2):
        qntd_latas_copos = input()
        qntd_latas_copos = list(map(int,qntd_latas_copos.split()))
        if qntd_latas_copos[0] > qntd_latas_copos[1]:
            cont += qntd_latas_copos[1]
        break
print(cont)


