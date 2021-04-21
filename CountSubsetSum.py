def countSubset(arr,n,s):
    if(n<0 and s!=0):
        return 0
    elif(s==0):
        return 1
    elif( arr[n]<=s ):
        return countSubset(arr, n-1, s-arr[n]) + countSubset(arr, n-1, s)
    else:
        return countSubset(arr, n-1, s)
 
    
def countSubsetMx(arr,n,s):
    dp = [[0 for j in range(s+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(s+1):
            if(i==0 and j!=0):
                dp[i][j]=0
            elif( j==0 ):
                dp[i][j] = 1
            elif(arr[i-1]<=j):
                dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]
                
    print(dp[n][s])
    

arr = [1,2,7,4,6,10]
s = 20

c = countSubset(arr, len(arr)-1, s) 

print(c)

countSubsetMx(arr, len(arr), s)