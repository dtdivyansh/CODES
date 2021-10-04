def sumOfSlope(a,b):
    ans =0
    for num in range(a,b+1):
        s = [i for i in str(num)]
        p = 0
        for i in range(1,len(s)-1):
            a = int(s[i-1])
            b = int(s[i])
            c = int(s[i+1])
            
            if(a<b and c<b):
                p+=1
                
            if(a>b and c>b):
                p+=1
                
        ans = ans + p
    
    return ans

print( sumOfSlope(150, 200) )
            
