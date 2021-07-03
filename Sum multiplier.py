def sumMultiplier(arr):
    arr = [int(i) for i in arr.split(',')]
    n = len(arr)
    s=0
    sumi = sum(arr)*2
    arr.sort()
    i,j=0,n-1
    while(i<j):
        val = arr[i]*arr[j]
        if(val>sumi):
            return 'true'
        else:
            i+=1
    return 'false'

print(sumMultiplier(input()))
