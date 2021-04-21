def eqSumSet(arr,n,s1,l):
    if(n<0 or len(l)>2):
        return 0
    elif(s1==arr[n] and len(l)==1):
        l.append(arr[n])
        print("selected: ",l)
        return 1
    a = [i for i in l ]
    a.append(arr[n])
    return eqSumSet(arr,n-1,arr[n]+s1,a) + eqSumSet(arr,n-1,arr[n]-s1,a) + eqSumSet(arr,n-1,s1,l)

    
arr = [int(i) for i in input().split()]
s1 = int(input())
n = len(arr)
l = list()
print(eqSumSet(arr,n-1,s1,l))