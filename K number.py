def Knumber(k,n):
    for i in range(1,10000000):
        if( i%k==0 or str(k) in str(i) ):
            n-=1
        if(n==0):
            return i
