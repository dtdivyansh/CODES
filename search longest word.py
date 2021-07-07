def search(sen):
    s = ''
    c = 0
    cm = 0
    sm = ''
    for i in sen:
        if(i==' '):
            if(c>cm and s.isalnum()):
                cm = c
                sm = s
            c=0
            s=''
        else:
            s+=i
            c+=1
    if(c>cm and s.isalnum()):
        cm = c
        sm = s
    return sm

print( search(input()) )
