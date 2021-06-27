f = {}
w = {}

def factors(n):
    ans = []
    i=1
    while(i*i<=n):
        if(n%i==0):
            ans.append(i)
            if(n//i!=i and n//i!=n):
                ans.append(n//i)
        i+=1
    return ans

def ways(n,x):
    if(n==1):
        return 1
    else:
        if(n not in f.keys()):
            fac = factors(n)
            f[n]=fac
        else:
            fac = f[n]
        m = 0
        for i in fac:
            if((i,x) in w.keys()):
                a = w[(i,x)]
            else:
                a = (x//i) + ways(i,x)
            m = max(m,a)
            
        w[(i,x)]=m
        return m


arr = [int(i) for i in input().split()]
res = 0

for i in arr:
    res = res + ways(i,i)
print(res)
