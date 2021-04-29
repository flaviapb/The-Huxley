while True:
    multi = int(input()) #multiplicador
    if multi != 0:
        matriz = [[],[],[],[]]
        for l in range(4):
            for c in range(4):
                if l == c:
                    matriz[c].append(int(input())*multi)
                else:
                    matriz[c].append(int(input()))
    else:
        break
    for i in range(4):
        for j in range(4):
            print(matriz[i][j], end=' ')
        print()


