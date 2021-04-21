v = []
def eqSum(arr,n,s,box):
    if(n<0):
        return False
    elif(s==0):
        v.append(box)
    elif(arr[n]<=s):
        eqSum(arr, n-1, s,box)
        t = box.copy()
        t.append(arr[n])
        eqSum(arr,n-1,s-arr[n],t)
    elif(arr[n]>s):
        return eqSum(arr, n-1, s,box)
    
arr = [1,5,11,23,12,42,35,36,34,9]
s = sum(arr)
print(s)
if(s&1):
    print('Cant be partitioned equally')
else:
    eqSum(arr, len(arr)-1, s//2,[])
    if(v):
        print(v)   
    else:
        print('Cant be partitioned equally')

