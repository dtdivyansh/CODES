import gc
from sys import stdin
for i in range(int(input())):
    temp = input().split()
    s = temp[1]+temp[2]
    k,d1,d2 = int(temp[0]),int(temp[1]),int(temp[2])
    print(k ,d1,d2)
    flag = d1+d2
    while(k>2):
        add = flag%10
        s = s + str(add)
        flag = flag + add
        print("hey",s,add)
        k-=1
        gc.collect()
    print(s ,d1,d2)
    if(int(s)%3==0):
        print("YES")
    else:
        print("NO")