def f(arr):

    def coprime(a,b):
        if(a==0 or b==0):
            return 0
    
        if(a==b):
            return b
    
        if(a>b):
            return coprime(a-b,b)
        else:
            return coprime(a,b-a)
    
    val = [i for i in range(2,251)]
    
    for x in range(0,len(arr)):
        v = arr[x]
        ans = 0
        res=0
        for k in val:
            if( coprime(v,k)==1 ):
                if(ans<abs(v-k)):
                    ans = abs(v-k)
                    res = k
        arr[x] = res
    
    return arr
