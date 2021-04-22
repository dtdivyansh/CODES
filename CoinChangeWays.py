mem = [[-1 for i in range(100)] for j in range(100)]  # MEMOIZATION

def ways(coins,n,change):
    if(change==0 and n>0):
        mem[n][change] = 1
        return 1
    elif(n<=0):
        mem[n][change]= 0
        return 0
    elif(coins[n-1]<=change):
        mem[n][change] = ways(coins, n, change-coins[n-1]) + ways(coins, n-1, change)
    else:
        mem[n][change]= ways(coins, n-1, change)
    return mem[n][change]

def waysMx(coins,n,change):  # TOP-DOWN APPROACH
    dp = [[-1 for j in range(change+1)] for i in range(n+1)]
    
    for i in range(n+1):
        for j in range(change+1):
            if(j==0 and i>0):
                dp[i][j]=1
            elif(i==0):
                dp[i][j]=0
            elif(coins[i-1]<=j):
                dp[i][j] = dp[i][j-coins[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    print(dp[n][change])

    
coins = [1,2,4,5]
change = 10
n = len(coins)

out = ways(coins, n, change)
print(out)

waysMx(coins, n, change)
