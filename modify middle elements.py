n = int(input())
arr = []
for i in range(n):
    arr.append( int(input()) )
    
if(n%2!=0):
    pass
else:
    v = n//2
    a = v-1
    ans = arr[v] + arr[a]
    
    arr.insert(v+1,ans)
    arr.pop(a)
    arr.pop(a)
    
for i in arr:
    print(i,end=' ')
    
