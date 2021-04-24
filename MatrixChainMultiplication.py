mem = [[-1 for j in range(1001)] for i in range(1001)] # MEMOIZATION

def multi(arr,i,j):
    if(mem[i][j]!=-1):
        return mem[i][j]
    if(i>=j):
        mem[i][j]=0
        return mem[i][j]
    else:
        mi = 10000007
        for k in range(i,j):
            t = multi(arr, i, k) + multi(arr, k+1, j) + arr[i-1]*arr[k]*arr[j]
            mi = min(t,mi)
        mem[i][j] = mi   
        return mem[i][j]

'''
def multiPrint(arr,i,j):
    dp = [[-1 for n in range(1001)] for m in range(1001)]
    for m in range(j):
        for n in range(j+1):
            if(m>=n):
                dp[m][n]=0
            else:
                t = 10000007
                for k in range(m,n):
                    v = dp[m][k] + dp[k+1][n]+ arr[m-1]*arr[k]*arr[n]
                    t = min(v,t)
                dp[m][n] = t
    print(dp[m][n])
'''
    
arr = [40,20,30,10,30]
i = 1
j = len(arr)-1

out = multi(arr, i, j)

print(out)
#multiPrint(arr, i, j)       