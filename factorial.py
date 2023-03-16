n = int(input('Number:'))
f = 1
while n > 1:
    f = f *n
    n = n - 1
print(f)

n = int(input('Number:'))
f = 1
for i in range (2,n+1):
    f = f * i
print (f)

import math
n = int(input('Number:'))
f = math.factorial(n)
print(f)
