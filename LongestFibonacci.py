def maxFibo(arr):
    
    S = set(arr)
    n = len(arr)
    mx = 0
    for i in range(n):
        for j in range(i+1,n):
            x = arr[j]
            y = arr[j] + arr[i] 
                
            l = 2
                
            while(y in S):
                z = x+y
                x = y
                y = z
                l+=1
                if(l>mx):
                    mx=l
                        
    return mx if mx>=3 else 0
        
arr = [1,2,7,4,5,8,9,15,23]
val = maxFibo(arr)

print(val)