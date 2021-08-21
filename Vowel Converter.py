def Vowel(str):
    vow = 'aeiou'
    res = ''
    if(str[0] in vow):
        flag=1
        res+='V'
    else:
        flag=0
        res+='C'
    for i in str[1:]:
        if(i in vow):
            if(flag==0):
                res+='V'
                flag=1
        else:
            if(flag==1):
                res+='C'
                flag=0
                
    return res
