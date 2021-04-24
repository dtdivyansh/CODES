# IT IS SAME AS MINIMUM NUMBER OF INSERTION

def lcs(a,b,m,n):
    if(m==0 or n==0):
        return 0
    elif(a[m-1]==b[n-1]):
        return 1 + lcs(a,b,m-1,n-1)
    else:
        return max( lcs(a,b,m-1,n) , lcs(a,b,m,n-1) )
    
def MinDelete(a,m):
    b = a[::-1]
    return m -  lcs(a,b,m,m)

a = 'ahgbcba'
m = len(a)

out = MinDelete(a, m)

print(out)