v = []
def eqSumSet(arr,n,s,box):
    if(n<0 and s!=0):
        return False
    if(s==0):
        v.append(box)
    elif(arr[n]<=s):
        t = box.copy()
        t.append(arr[n])
        eqSumSet(arr,n-1,s-arr[n],t)
        eqSumSet(arr,n-1,s,box)
    else:
        eqSumSet(arr,n-1,s,box)
    
def eqSumSetMx(arr,n,s1):
    mat = [[0 for j in range(s1+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(s1+1):
            if(i==0 and j!=0):
                mat[i][j]=0
            elif(j==0):
                mat[i][j]= 1
            elif(arr[i-1]<=j):
                mat[i][j] = mat[i-1][j-arr[i-1]] or mat[i-1][j]
            else:
                mat[i][j]=mat[i-1][j]
    f = []            
    for i in range(n,0,-1):
        j = s1
        i2 = i
        box = []
        while(j>0):
            if(mat[i2][j]==1):
                box.append(arr[i2-1])
                j = j - arr[i2-1]
                i2 = i2-1
            else:
                break
        if(box):
            f.append(box)      
    #print(mat)
    return f
                
        
    
arr = [int(i) for i in input().split()]
s = int(input())
n = len(arr)
eqSumSet(arr,n-1,s,[])
print(v)
print(eqSumSetMx(arr,n,s))
