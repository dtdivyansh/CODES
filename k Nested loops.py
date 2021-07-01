def loop(n,k):
    if(n==0):
        return
    else:
        print()
        for i in range(k):
            print('loop',n,i,end=" ")
            loop(n-1,k)
            
        print("******")

n = int(input())
loop(n,n)
