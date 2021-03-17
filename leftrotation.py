import numpy as np
# Complete the rotLeft function below.
def rotLeft(a, d):
    rotation = d % len(a)
    helpindex = [[0]]*len(a)
    if rotation == 0:
        return a
    for i in range (0, len(a)):
        helpindex[i] =a[ajustIndex(i+rotation,len(a))]
    return helpindex

def ajustIndex(index, length):
    if( index >= length):
        return index % length
    else:
        return index 

a = [41, 73, 89, 7, 10, 1, 59, 58, 84, 77, 77, 97, 58, 1, 86, 58, 26, 10, 86, 51]
b = 10
print(rotLeft(a,b))