def merge(arr,l,m, r):
    n1 = m-l+1
    n2 = r -m 

    #Crear arreglos temporales
    L = [0]*n1
    R = [0]*n2

    #Llenando los arreglos temp
    for i in range(0,n1):
        L[i] = arr[l+i]
    for j in range(0,n2):
        R[j] = arr[m+1+j]
    
    #Inicializamos de nuevo los iteradores
    i = 0 #Recorre L
    j = 0 #Recorre R
    k = l #Recorre array completo

    #Comparando item x item en L y R
    while(i < n1 and j < n2):
        if(L[i] <= R[j]):
            arr[k] = L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1 
        k+=1
    #Se agregan numeros sobrantes
    while(i < n1):
        arr[k] = L[i]
        i+=1
        k+=1
    while(j < n2):
        arr[k] = R[j]
        j+=1
        k+=1
def mergeSort(array,l,r):
    if(l < r):
        m = (l+(r-1))//2

        mergeSort(array, l, m)
        mergeSort(array, m+1, r)

        merge(array,l,m,r)

n = int(input("Len array:"))
array = [0]*n
for i in range (n):
    array[i] = input()
print(array)
mergeSort(array,0,n-1)
print("Sorted array")
#for i in range (n):
print(array)