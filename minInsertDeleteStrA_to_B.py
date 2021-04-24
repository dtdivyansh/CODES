def lcs(a,b,m,n):
    if(m==0 or n==0):
        return 0
    elif(a[m-1]==b[n-1]):
        return 1 + lcs(a,b,m-1,n-1)
    else:
        return max( lcs(a,b,m-1,n) , lcs(a,b,m,n-1) )
    
def InsDelMin(a,b,m,n):
    l = lcs(a, b, m, n)
    dele = m-l
    ins = n-l
    print('Insert: {} \nDelete: {}'.format(ins,dele))
    
a = 'adfghy'
m = len(a)
b = 'afgk'
n = len(b)

InsDelMin(a, b, m, n)