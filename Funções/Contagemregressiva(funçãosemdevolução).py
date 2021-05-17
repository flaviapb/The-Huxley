num = int(input())

def regressiva(n):
    for i in range(n,0,-1):
        cont = 1
        while True:
            if cont == i:
                print(i)
                break
            else:
                print(i, end="-")
            cont += 1

regressiva(num)