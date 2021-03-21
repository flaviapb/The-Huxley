"Desenvolvido por Flávia"

pequena = 0
grande = 0

for i in range(7):
  num = int(input())
  tamanho = input().upper()

  if tamanho == "P":
    pequena += 10 * num

  if tamanho == "G":
    grande += 16 * num

  total = pequena + grande



print(total)
print(int ((total * 2)/7))