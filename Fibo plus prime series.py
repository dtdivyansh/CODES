def fibo(n):
    a,b=1,1
    if(n==1 or n==2):
        return 1
    
    while(n-2>0):
        b = a+b
        a = b-a
        n-=1
        
    return b

def prime(n):
    j=10**6
    p = [0 for i in range(j+1)]
    ans = []
    c=0
    for i in range(2,j+1):
        if(p[i]==0):
            ans.append(i)
            c+=1
            if(c>=n):
                break
            for k in range(i*i,j+1,i):
                p[k]=1
         
    return ans[n-1]

n = int(input())

if(n&1):
    print( fibo(n//2+1) )
else:
    print( prime(n//2) )
