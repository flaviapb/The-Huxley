t1  =  0
t2  =  0
t3  =  0
t4  =  0
t5  =  0

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())

for i in range(1, num1+1):
  if ( num1 % i  ==  0 ):
        t1  +=  i
for i in range(1, num2+1):
  if ( num2 % i  ==  0 ):
        t2  +=  i
for i in range(1, num3 +1):
  if ( num3 % i  ==  0 ):
        t3  +=  i
for i in range(1, num4+1):
  if ( num4 % i  ==  0 ):
        t4  +=  i
for i in range(1, num5+1):
  if ( num5 % i  ==  0 ):
        t5 +=  i

if ( t1 >= t2  and  t1 >= t3  and  t1 >= t4  and  t1 >= t5 ):
    print(num1)
elif ( t2 >= t1  and  t2 >= t3  and  t2 >= t4  and  t2 >= t5 ):
    print(numw)
elif ( t3 >= t1  and  t3 >= t2  and  t3 >= t4  and  t3 >= t5 ):
    print(num3)