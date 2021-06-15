def solve(arr,r,c,n):
    if(r==n-1 and c==n-1 and arr[r][c]==1):
        arr[r][c]=2
        return True
    if(r>=n or c>=n):
        return False
    else:
        if(arr[r][c]):
            k1=solve(arr,r+1,c,n)
            if(k1):
                arr[r][c]=2
                return True
            k2=solve(arr,r,c+1,n)
            if(k2):
                arr[r][c]=2
                return True
            else:
                arr[r][c]=0
                return False
        else:
            return False

n = int(input())
arr = []
for i in range(n):
    val = [int(j) for j in input().split()]
    arr.append(val)
    
c=0
r=0
solve(arr,r,c,n)
for i in range(n):
    for j in range(n):
        if(arr[i][j]==2):
            arr[i][j]=1
        else:
            arr[i][j]=0
            
for i in range(n):
    for j in range(n):
        print(arr[i][j],end=" ")
    print()
