# TOP-DOWN APPROACH
def RodCutMx(wt,val,n,W):
    print(n,W)
    dp = [[-1 for j in range(W+1)] for i in range(n+1) ]
    
    for i in range(n+1):
        for j in range(W+1):
            if(j==0):
                dp[i][j]=0
            elif(i==0):
                dp[i][j]=0
            elif(wt[i-1]<=j):
                dp[i][j] = max( dp[i-1][j], val[i-1]+dp[i][j-wt[i-1]] )
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[n][W])


l = [1,3,4,5,8]
price = [2,7,4,5,8]
length = 8
n = len(l)
RodCutMx(l,price,n,length)
