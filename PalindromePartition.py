def isPali(s,i,j):
    while(i<j):
        if(s[i]!=s[j]):
            return False
        i+=1
        j-=1
    return True


mem = [[-1 for j in range(1001)] for i in range(1001)]
def partition(s,i,j):
    if(mem[i][j]!=-1):
        return mem[i][j]
    if(i>=j):
        mem[i][j]=0
        return 0
    elif( isPali(s, i, j) ):
        mem[i][j]=0
        return 0
    else:
        mn = 100000007
        for k in range(i,j):
            t = partition(s, i, k) + partition(s, k+1, j) + 1
            mn = min(mn,t)
        mem[i][j]=mn
        return mn
    
s = 'Divyansh'
i = 0
j = len(s)-1

out = partition(s, i, j)

print(mem[i][j])          