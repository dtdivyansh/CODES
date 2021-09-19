t = input().split()

n = int(t[0])
q = int(t[1])

a = list( map( int, input().split() ))
l = input().split()

c = [26 for i in range(n)]

dic = {}

for i in range(q):
    if( (a[i],l[i]) not in dic.keys() ):
        dic[ (a[i],l[i]) ] = 1
        c[a[i]-1]-=1

ans = 1
for i in c:
    ans = ans*i

print(ans)
