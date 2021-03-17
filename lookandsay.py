
def lookandsay(n, cad):
    times=1
    i=0
    if(len(n)==0):
        return cad
    if(len(n)==1):
        cad+="1"+str(n)
        return cad
    else:
        for i in range (0,len(n)-1):
            if(n[i]== n[i+1]):
                times+=1
            else:
                break 
        #print("i",i)        
        cad+=str(times)+str(n[i+1])
        #print(n[i+2:len(n)])
        return lookandsay(n[i+1:len(n)],cad)

def LS(n):
    cad=""
    result=n
    for i in range (0, 10):
        result=(lookandsay(result,cad))
        print(result)



n = input()
LS(n)
