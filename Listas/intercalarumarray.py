array1 = []
array2 = []


vezes = int(input())

for i in range(vezes):
    num1 = int(input())
    array1.append(num1)

for i in range(vezes):
    num2 = int(input())
    array2.append(num2)

 print([*sum(zip(array1,array2),())])

