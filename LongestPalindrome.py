def lcs(a,b,m,n):
    if(m==0 or n==0):
        return 0
    elif(a[m-1]==b[n-1]):
        return 1 + lcs(a,b,m-1,n-1)
    else:
        return max( lcs(a,b,m-1,n) , lcs(a,b,m,n-1) )
    
def lps(a,m):
    b = a[::-1]
    lpsPrint(a,b,m,m)
    return lcs(a,b,m,m)

def lpsPrint(a,b,m,n):
    dp = [[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if(i==0 or j==0):
                dp[i][j]=0
            elif(a[i-1]==b[j-1]):
                dp[i][j]=1 + dp[i-1][j-1]
            else:
                dp[i][j] = max( dp[i-1][j] , dp[i][j-1] )
                
    # PRINTING
    i=m
    j=n
    s = ''
    while(i>0 and j>0):
        if(a[i-1]==b[j-1]):
            s = a[i-1] + s
            i-=1
            j-=1
        else:
            if(dp[i][j-1]>dp[i-1][j]):
                j-=1
            else:
                i-=1
    print(s)


a = 'agbbca'
m = len(a)

out = lps(a,m)

print(out)
    