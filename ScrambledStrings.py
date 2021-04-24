mem = {}

def scramble(a,b):
    if((a,b) in mem.keys()):
        return mem[(a,b)]
    if(a==b):
        mem[(a,b)] = True
        return mem[(a,b)]
    elif(len(a)==1):
        mem[(a,b)] = False
        return mem[(a,b)]
    else:
        boo = False
        for i in range(1,len(a)):
            sol1 = scramble(a[0:i], b[len(b)-i:]) and scramble(a[i:], b[0:len(b)-i])
            sol2 = scramble(a[0:i], b[0:i]) and scramble(a[i:], b[i:])
            if(sol1 or sol2):
                boo = True
                break
        mem[(a,b)] = boo
        return mem[(a,b)]
    
a = 'great'
b = 'greta'

if(len(a)!=len(b)):
    print('Not Scramble')
elif(a=='' and b==''):
    print('Scramble')
else:
    if(scramble(a, b)):
        print('Scramble')
    else:
        print('Not Scramble')
    print(mem[(a,b)])