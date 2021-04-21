def eqSumSet(arr,n,s1):
    if(s1==0):
        return True
    elif(n<0):
        return False
    elif(arr[n]<=s1):
        return eqSumSet(arr,n-1,s1-arr[n]) or eqSumSet(arr,n-1,s1)
    else:
        return eqSumSet(arr,n-1,s1)
    
def eqSumSetMx(arr,n,s1):
    mat = []
    for i in range(n+1):
        mat.append([])
        for j in range(s1+1):
            if(i==0 and j!=0):
                mat[i].append(0)
            elif(j==0):
                mat[i].append(1)
            elif(j-arr[i-1]>=0):
                mat[i].append( mat[i-1][j] or mat[i-1][j-arr[i-1]] )
            else:
                mat[i].append(mat[i-1][j])
                
    #for i in range(n+1):
     #   for j in range(m+1):
      #      print(mat[i][j],end=",")
       # print()
    return mat[n][s1]
                
        
    
arr = [int(i) for i in input().split()]
s1 = int(input())
n = len(arr)
print(eqSumSet(arr,n-1,s1))
print(eqSumSetMx(arr,n,s1))
