n = int(input())

for i in range(1,10**5):
    v = i*i
    if(v>n):
        print(v)
        break
