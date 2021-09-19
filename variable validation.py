def check(var):
    if( var[0].isdigit() ):
        return False
    
    for s in var[1:]:
        if( s.isalpha() or s=='_' or s.isdigit() ):
            continue
        else:
            return False
    
    return True
            
var = input()

print( check(var) )
