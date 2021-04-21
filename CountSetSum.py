def eqSumSet(arr,n,s1):
    if(s1==0):
        return 1
    elif(n<0):
        return 0
    elif(arr[n]<=s1):
        return eqSumSet(arr,n-1,s1-arr[n]) + eqSumSet(arr,n-1,s1)
    else:
        return eqSumSet(arr,n-1,s1)
    

def eqSumSetMx(arr,n,s1):
    mat = []
    for i in range(n+1):
        mat.append([])
        for j in range(s1+1):
            if(j==0):
                mat[i].append(1)
            elif(i==0):
                mat[i].append(0)
            elif(arr[i-1]<=j):
                mat[i].append( mat[i-1][j] + mat[i-1][j-arr[i-1]] )
            else:
                mat[i].append( mat[i-1][j] )
    return mat[n][s1]
                
            

arr = [int(i) for i in input().split()]
s1 = int(input())
n = len(arr)
print(eqSumSet(arr,n-1,s1))
print(eqSumSetMx(arr,n,s1))