arr = [int(i) for i in input().split()]
x = int(input())
prev = arr.copy()
flag=False
for i in range(1,len(arr)):
    if(arr[i]>arr[i-1]):
        if(arr[i-1]==prev[i-1]):
            if(i==1):
                if(arr[i-1]+x> arr[i]):
                    arr[i-1]+=x
                    continue
            else:
                if(arr[i-1]+x> arr[i] and arr[i-1]+x < arr[i-2]):
                    arr[i-1]+=x
                    continue
        else:
            arr[i]-=x
            continue

for i in range(1,len(arr)):
    if(arr[i]>=arr[i-1]):
        flag=True
        break
    
if(flag):
    print('NO')
else:
    print('YES')
