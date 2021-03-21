"Desenvolvido por Flávia"


maior_distancia = 0
destino_final = " "

while True:

  cidade = input().upper()
  if cidade == "FIM":
    break

  distancia = int(input())
  passagem = float(input())

  if (passagem * 2 <= 300) and (distancia > maior_distancia):
    maior_distancia = distancia 
    destino_final = cidade 

if destino_final == " ":
    print("SEM DESTINO")

else:
    print(destino_final)