def search(sen):
    c = 0
    for i in sen:
        if( i.isalpha() ):
            if(c>1):
                return True
            c=0
        elif( i.isdigit() ):
            if( int(i)%2==0 ):
                c+=1
            if(c>1):
                return True
    return False
                

print( search(input()) )
