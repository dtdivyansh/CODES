v = []
def eqSumSet(arr,n,s,box):
    if(n<0 and s!=0):
        return False
    if(s==0):
        v.append(box)
    elif(arr[n]<=s):
        t = box.copy()
        t.append(arr[n])
        eqSumSet(arr,n-1,s-arr[n],t)
        eqSumSet(arr,n-1,s,box)
    else:
        eqSumSet(arr,n-1,s,box)
    
def eqSumSetMx(arr,n,s1):
    mat = [[0 for j in range(s1+1)] for i in range(n+1)]
    box = []
    for i in range(n+1):
        for j in range(s1+1):
            if(j==0):
                v.append(box)
            elif(arr[i-1]<=j):
                box.append(arr[n-1])
            else:
                pass
                
        
    
arr = [int(i) for i in input().split()]
s = int(input())
n = len(arr)
eqSumSet(arr,n-1,s,[])
print(v)
#print(eqSumSetMx(arr,n,s))
