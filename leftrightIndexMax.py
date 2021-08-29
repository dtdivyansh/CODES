def f(arr):
    m = -1
    
    for i in range(len(arr)):
        l,r=0,0
        
        for k in range(i-1,-1,-1):
            if(arr[k]>arr[i]):
                l=k
                break
            
        for j in range(i+1,len(arr)):
            if(arr[j]>arr[i]):
                r=j
                break
            
        m = max(m,l*r)
    
    return m

print(f([1,5,4,3,5,2]))
