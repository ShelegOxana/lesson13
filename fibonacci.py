n1 = n2 = 1
n = int(input('Number of elements: '))
for i in range(2, n):
    n1, n2 = n2, n1 + n2
    print (n2, end=' ')





