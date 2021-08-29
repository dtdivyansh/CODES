def f(lst):
    if(not lst):
        return -1
    
    s=0
    i=0
    nt=0
    for t in lst:
        a = t.s1 
        b = t.s2
        c = t.s3
        if(a+b>c or a+c>b or b+c>a):
            
            if(a!=b and a!=c and b!=c):
                s+=1
                
            elif(a==b or b==c or a==c):
                i+=1
                
        else:
            nt+=1
    
    return 3*s -(i+nt)
