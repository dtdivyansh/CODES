mem = [[-1 for i in range(11)] for j in range(21)] # MEMOIZATION

def Unbound(wt,val,n,W):
    if(mem[n][W]!=-1):
        return mem[n][W]
    if(n==0):
        mem[n][W]=0
        return 0
    elif(W==0):
        mem[n][W]=0
        return 0
    elif(wt[n-1]<=W):
        mem[n][W]= max( Unbound(wt, val, n-1, W) , val[n-1]+Unbound(wt, val, n, W-wt[n-1]))
    else:
        mem[n][W]= Unbound(wt, val, n-1, W)
        
    return mem[n][W]
    
# TOP-DOWN APPROACH
def UnboundMx(wt,val,n,W):
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
    

    
wt = [2,4,5,6,7,3]
val = [2,3,2,3,4,50]
W = 6
n = len(wt)
out = Unbound(wt, val, n, W)
print(out)
UnboundMx(wt, val, n, W)