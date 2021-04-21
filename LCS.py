dp = [[0 for i in range(m+1)] for j in range(n+1)]
def lcs(self,m,n,X,Y):
        global dp
        if(m==0 or n==0):
            return 0
            
        elif(dp[m][n]!= 0 ):
            return dp[m][n]
        
        elif( X[m-1] == Y[n-1] ):
            dp[m][n] =  1 + self.lcs(m-1,n-1,X,Y)
            #print('hey',X[m-1],m,n)
        else:
            dp[m][n]= max( self.lcs(m,n-1,X,Y) , self.lcs(m-1,n,X,Y) )
            
        if(m==len(X) and n==len(Y)):
            temp = dp[m][n]
            dp = [[0 for i in range(m+1)] for j in range(n+1)]
            return temp
        else:
            return dp[m][n]
        
"""
dp = [[0 for i in range(m+1)] for j in range(n+1)]
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                if( Y[i-1] == X[j-1] ):
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max( dp[i-1][j],dp[i][j-1] )
"""
'''
def longest(s1,s2,i,j):
    if(len(s1)==0 or len(s2)==0):
        return ''
    elif(i<0 or j<0):
        return ''
    else:
        c = ''
        if(s1[i]==s2[j]):
            c=longest(s1,s2,i-1,j-1)+s1[i]
        a=longest(s1,s2,i,j-1)
        b=longest(s1,s2,i-1,j)
        a1 = len(a)
        b1 = len(b)
        c1 = len(c)
        if(a1>b1):
            if(a1>c1):
                return a
            else:
                return c
        elif(b1>c1):
            return b
        else:
            return c
            
s1 = input()
i = len(s1)-1
s2 = input()
j = len(s2)-1
s = longest(s1,s2,i,j)
print(s)
'''
