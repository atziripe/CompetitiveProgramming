import numpy as np
def aVeryBigSum(ar):
    sum = 0
    for i in range (0, len(ar)):
        sum += ar[i]
    return sum

n= int(input("n: "))
ar = np.zeros(n)
print(len(ar))
for i in range (0,len(ar)):
    ar[i]= int(input())
result = aVeryBigSum(ar)
print(result)