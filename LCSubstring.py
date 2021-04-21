def longestCommonSubstr(self, S1, S2, n, m):
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
    
"""
def longestCommonSubstr(self, S1, S2, n, m):
        global c
        global ma
        if( n==0 or m==0 ):
            return 0
        
        if( S1[n-1]==S2[m-1] ):
            c+=1
            if(ma<c):
                ma=c
            self.longestCommonSubstr(S1,S2,n-1,m-1)
            
        else:
            c=0
            self.longestCommonSubstr(S1,S2,n,m-1)
            self.longestCommonSubstr(S1,S2,n-1,m)
            
        if(len(S1)==n and len(S2)==m):
            c=0
            m2 = ma
            ma=0
            return m2
        else:
            return ma
            
"""