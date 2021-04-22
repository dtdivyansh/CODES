# MEMOIZATION
mem = [[-1 for i in range(1000)] for j in range(1000)]
def minCoins(coins,n,change,c):
    if(change==0):
        mem[n][change]= c
        return mem[n][change]
    elif(n<=0):
        mem[n][change]= 1000007
        return mem[n][change]
    elif(coins[n-1]<=change):
        mem[n][change]= min( minCoins(coins,n,change-coins[n-1],c+1) , minCoins(coins,n-1,change,c))
    else:
        mem[n][change]= minCoins(coins,n-1,change,c)
    return mem[n][change]

#TOP-DOWN APPROACH
def minCoinsMx(coins,n,change):
    dp = [[-1 for j in range(change+1)] for i in range(n+1)]
    
    for i in range(n+1):
        for j in range(change+1):
            if(j==0):
                dp[i][j]= 0
            elif(i==0):
                dp[i][j]= 1000007
            elif(coins[i-1]<=j):
                dp[i][j] = min(1+dp[i][j-coins[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    print(dp[n][change]) 
    
    
coins = [1,5,10]
change = 18
n = len(coins)

out = minCoins(coins,n,change,0)
print(out)

minCoinsMx(coins,n,change)