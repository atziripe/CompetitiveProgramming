import numpy as np
def isInvalid(m,r,c):
   return r<0 or c<0 or r>=len(m) or c>= len(m) or m[r][c] != 0

def doSpiralArray(n):
    dc =[1,0,-1,0]
    dr =[0,1,0,-1]
    dire = 0
    val= 0
    r=0
    c=0
    limit=n*n
    matrix = np.zeros((n,n))
    for val in range(0, limit):
        matrix[r][c] = val+1
        print("val: ",val, " r: ", r, " c: ", c)
        r += dr[dire]
        c += dc[dire]
        if (isInvalid(matrix,r, c)):
            r-= dr[dire]
            c-=dc[dire]
            dire = (dire+1)%4
            r+= dr[dire]
            c+= dc[dire]
    return matrix


n = int(input("n:"))
while(n <= 0):
    print("n hast to be bigger than 0")
    n = int(input())
print(doSpiralArray(n))
