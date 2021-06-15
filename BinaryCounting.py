temp = input().split()
r = int(temp[0])
k = int(temp[1])
ans=0
for i in range(1,r+1):
    bi = bin(i)
    res = bi[2:]
    l = 0
    r = 2
    c=0
    while(r<len(res)):
        if(res[l:r+1]=='101'):
            c+=1
        r+=1
        l+=1
    if(c>=k):
        ans+=1
        
print(ans)
