"Desenvolvido por Flávia"

divida =  int(input())
pagamento =  int(input())

while divida > 0 :
    print ("(antes) {}" .format(divida))
    
    if divida <= pagamento:
        divida =  0
    else:
        divida -= pagamento
    print ("(depois) {}" .format(divida))