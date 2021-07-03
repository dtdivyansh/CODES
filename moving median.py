def movingMedian(arr):
    arr = [int(i) for i in arr.split(',')]
    size = arr.pop(0)
    s = arr[0]
    res = str(arr[0])
    i,j = 0,1
    l = len(arr)
    while(j<l):
        s = s+arr[j]
        n = j-i+1
        a = s//n
        if(a<0):
            res = res+','+'0'
        else:    
            res = res+','+str(a)
        if(n < size):
            j+=1
        else:
            j+=1
            i+=1
    return res

print(movingMedian(input()))
