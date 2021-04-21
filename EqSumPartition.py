def eqSum(arr,n,s):
    if(n<0):
        return False
    if(arr[n]==s):
        return True
    if(arr[n]<s):
        return eqSum(arr,n-1,s-arr[n]) or eqSum(arr, n-1, s)
    if(arr[n]>s):
        return eqSum(arr, n-1, s)
    
arr = [1,6,3]
s = sum(arr)

if(s&1):
    print('Cant be partitioned equally')
else:
    out = eqSum(arr, len(arr)-1, s//2)
    if(out):
        print('Can be partitioned')
    else:
        print('Cant be partitioned equally')
    