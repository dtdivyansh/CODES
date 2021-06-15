def lcs(m,n,X,Y): 
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if( Y[i-1] == X[j-1] ):
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max( dp[i-1][j],dp[i][j-1] )
        return dp[n][m]

def lcsub(n,m,S1,S2):
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        c=0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if( S1[i-1]==S2[j-1] ):
                    dp[i][j] = 1 + dp[i-1][j-1]
                    if( dp[i][j]>c ):
                        c=dp[i][j]
                else:
                    dp[i][j] = 0
        return c    

s1 = input()
s2 = input()
subseq = lcs(len(s1),len(s2),s1,s2)
substr = lcsub(len(s1),len(s2),s1,s2)
print(abs(subseq-substr))
