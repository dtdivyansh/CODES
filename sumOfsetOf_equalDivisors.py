def f(arr):
    k = max(arr)
    s = 0
    for i in range(2,k+1):
        r = arr[0]%i
        flag=1
        for j in range(1,len(arr)):
            if(arr[j]%i != r):
                flag=0
                break
            
        if(flag):
            s+=i
    
    return s
