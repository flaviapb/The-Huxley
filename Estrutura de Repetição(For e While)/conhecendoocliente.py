"Desenvolvido por Flávia"

qntd_compra_av = 0
qntd_compra_ca = 0
valor_total_av = 0
valor_total_ca = 0
media_a_vista = 0
idade_menor =  []
maior_compra = []
while True: 
  idade = int(input())
  valor_compra = float(input())
  tipo_pagamento = input().upper()
  continuar = input().upper()
 
  #Quantidades de compras
  if tipo_pagamento == "V":
    qntd_compra_av += 1
  elif tipo_pagamento == "C":
    qntd_compra_ca += 1
  qntd_total_compras = qntd_compra_av + qntd_compra_ca

  #valor total no cart�o ou avista
  if tipo_pagamento == "C":
    valor_total_ca += valor_compra
  elif tipo_pagamento == "V":
    valor_total_av += valor_compra
  
  #IDADE DO CLIENTE MAIS NOVO 
  idade_menor.append(idade)
  
  #Maior compra 
  maior_compra.append(valor_compra)
  
  #media das compras � vista
  if tipo_pagamento == "V":
    media_a_vista = valor_total_av / qntd_compra_av 
  
  #parar programa 
  if continuar == "N":
    break
      

     
    
 
print(qntd_total_compras)
if valor_total_av == 0:
  print(0)
else:
  print("{:.2f}".format(valor_total_av))
if valor_total_ca == 0:
  print(0)
else:
  print("{:.2f}".format(valor_total_ca))
print(min(idade_menor))
print("{:.2f}".format(max(maior_compra)))
if media_a_vista == 0:
  print(0)
else:
  print("{:.2f}".format(media_a_vista))