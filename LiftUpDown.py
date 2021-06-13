s = [i for i in input()]
c = 0
l = len(s)

for i in range(l):
    if(s[i]=='U'):
        v = l-i-1
        c+=v
        if('D' in s[i+1:] and i!=0):
            v = i+1
            c+=v
            
    else:
        v = i
        c+=v
        if('U' in s[:i] and i!=l-1):
            v = l-i+1+1
            c+=v
print(c)            
