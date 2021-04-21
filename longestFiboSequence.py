def findFibo(arr,n):
    val = []
    m = 0
    for i in range(n-2):
        for j in range(i+1,n-1):
            x = arr[i]
            y = arr[j]
            z = x+y
            l=2
            li = [x,y]
            while(z in arr):
                li.append(z)
                x = y
                y = z
                z = x+y
                l+=1
            if(l>m):
                m=l
                val = li
            elif(l==m):
                val = val if sum(val)<sum(li) else li
                
    return val
                
    
    
arr = [1,2,3,4,6,7,10]

v = findFibo(arr,len(arr))

print(v)
        