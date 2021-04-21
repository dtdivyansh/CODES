def longest(s1,s2,i,j):
    if(len(s1)==0 or len(s2)==0):
        return ''
    elif(i<0 or j<0):
        return ''
    else:
        c = ''
        if(s1[i]==s2[j]):
            c=longest(s1,s2,i-1,j-1)+s1[i]
        a=longest(s1,s2,i,j-1)
        b=longest(s1,s2,i-1,j)
        a1 = len(a)
        b1 = len(b)
        c1 = len(c)
        if(a1>b1):
            if(a1>c1):
                return a
            else:
                return c
        elif(b1>c1):
            return b
        else:
            return c
            
s1 = input()
i = len(s1)-1
s2 = input()
j = len(s2)-1
s = longest(s1,s2,i,j)
print(s)