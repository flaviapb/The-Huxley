"Desenvolvido por Flávia"

num = int(input())
while num != 0 :
  if num == 1:
    print("0")
  elif ( num  >  1 ):
    anterior =  0
    proximo =  1
    print ('{} {}'.format(anterior,proximo),end='')
    cont  =  3
    while ( cont <= num ):
            soma  =  anterior + proximo
            print (' {}'.format(soma),end='')
            anterior = proximo
            proximo = soma
            cont += 1
    print("")
  num = int(input())