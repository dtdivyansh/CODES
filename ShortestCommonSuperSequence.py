def lcs(a,b,m,n):
    if(m==0 or n==0):
        return 0
    elif(a[m-1]==b[n-1]):
        return 1 + lcs(a,b,m-1,n-1)
    else:
        return max( lcs(a,b,m-1,n) , lcs(a,b,m,n-1) )
    

def SCSPrint(a,b,m,n):
    dp = [[-1 for j in range(n+1)] for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if(i==0 or j==0):
                dp[i][j]=0
            elif(a[i-1]==b[j-1]):
                dp[i][j] = 1 + dp[i-1][j-1]
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
                s = b[j-1] + s
                j-=1
            else:
                s = a[i-1] + s
                i-=1
    while(i>0):
        s = a[i-1]+s
        i-=1
    while(j>0):
        s = b[j-1]+s
        j-=1
    print(s)
    


def shortSuper(a,b,m,n):
    l = lcs(a,b,m,n)
    return m + n - l

a = 'acb'
m = len(a)
b = 'acc'
n = len(b)

out = shortSuper(a, b, m, n)
SCSPrint(a, b, m, n)
print(out)