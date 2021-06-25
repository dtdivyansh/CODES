arr = [int(i) for i in input().split()]
n = len(arr)

new = [0 for i in range(n+2)]
new[0]=1

for i in arr:
    new[i]=1
    
ans = new.index(0)

print(ans)
