def lcs(a,b,m,n):
    if(m==0 or n==0):
        return 0
    elif(a[m-1]==b[n-1]):
        return 1 + lcs(a,b,m-1,n-1)
    else:
        return max( lcs(a,b,m-1,n) , lcs(a,b,m,n-1) )
    
a = 'ahbma'
m = len(a)
b = 'ahgbcba'
n = len(b)

out = lcs(a,b,m,n)

if( out==m ):
    print('{} is in {}'.format(a,b))
else:
    print('{} is NOT in {}'.format(a,b))