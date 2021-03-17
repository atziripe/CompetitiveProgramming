def mayor(arr, n):
    mayor  = 0
    for i in range (0,n):
        if(arr[i]>mayor):
            mayor = arr[i]
    return mayor

def arrayManipulation(n, queries):
    array = [0]*n
    for i in range (0, len(queries)):
        for j in range (queries[i][0], queries[i][1]+1):
            array[j-1] += queries[i][2]
    return max(array)
        
res =input().split()
queries = [[0] * 3 for i in range(int(res[1]))]
for i in range (0,int(res[1])):
    item = input().split()
    queries[i][0]= int(item[0])
    queries[i][1]= int(item[1])
    queries[i][2]= int(item[2])

print(arrayManipulation(int(res[0]),queries))