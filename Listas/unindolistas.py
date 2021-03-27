lista1 = []
lista2 = []
lista3 = []

while True:
    qntd_lista1 = int(input())
    if qntd_lista1 == 0:
        print("Erro - A lista deve ter pelo menos 1 elemento.")
        break
   
    else:
        for i in range(qntd_lista1):
            num1 = int(input())
            lista1.append(num1)
    
        qntd_lista2 = int(input())
        if qntd_lista2 == 0:
            print("Erro - A lista deve ter pelo menos 1 elemento.")
            break
   
        else:
            for i in range(qntd_lista2):
                num2 = int(input())
                lista2.append(num2)
            
            
        lista3 = lista1 + lista2

        print(* lista3, sep=" ")

        break

