ordem = int(input())
matriz = []
cont = 1

for i in range(ordem):
  linha = []
  for j in range(ordem):
    linha.append(cont)
    cont += 1
  matriz.append(linha)

print("Matriz:")
for i in range(ordem):
  for j in range(ordem):
    print('  {}'.format(matriz[i][j]), end='')
  print()

multiplicador = 1
somador = 0
print('\nDiagonal Principal:')
for i in range(ordem):
  print('  ' * multiplicador + ' ' * somador + '{}'.format(matriz[i][i]))
  multiplicador += 1
  somador += 1

print('\nDiagonal Secundaria:')
for i in range(ordem):
  multiplicador -= 1
  somador -= 1
  print('  ' * multiplicador + ' ' * somador + '{}'.format(matriz[i][-i - 1]))
