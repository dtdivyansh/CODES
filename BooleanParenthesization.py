mem = {}

def parenCheck(s,i,j,boo):
    if( (i,j,boo) in mem.keys() ):
        return mem[(i,j,boo)]
    if(i>j):
        mem[(i,j,boo)] = True
        mem[(i,j,not boo)] = True
        return mem[(i,j,boo)]
    elif(i==j):
        if(boo==True):
            mem[(i,j,boo)] = s[i]=='T'
            return mem[(i,j,boo)]
        else:
            mem[(i,j,boo)] = s[i]=='F'
            return mem[(i,j,boo)]
    else:
        res = 0
        for k in range(i+1,j,2):
            trueLeft = parenCheck(s, i, k-1, True) 
            trueRight = parenCheck(s, k+1, j, True)
            falseLeft = parenCheck(s, i, k-1, False) 
            falseRight = parenCheck(s, k+1, j, False)
            if(s[k]=='&'):
                if(boo==True):
                    res = res + int(trueLeft)*int(trueRight)
                else:
                    res = res + int(trueLeft*falseRight)+ int(trueRight*falseLeft)+ int(falseLeft*falseRight)
                    
            if(s[k]=='|'):
                if(boo==True):
                    res = res + int(trueLeft)*int(trueRight)+ int(trueLeft*falseRight)+ int(trueRight*falseLeft)
                else:
                    res = res + int(falseLeft*falseRight)
            
            if(s[k]=='^'):
                if(boo==True):
                    res = res + int(trueLeft*falseRight)+ int(trueRight*falseLeft)
                else:
                    res = res + int(falseLeft*falseRight)+ int(trueLeft)*int(trueRight)
        mem[(i,j,boo)] = res          
        return mem[(i,j,boo)]

    
s = 'F&F|T'
i = 0
j = len(s)-1
boo = True
out = parenCheck(s, i, j, boo)
print(out)
print(mem[(i,j,boo)])