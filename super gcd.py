def gcd(a,b):
    if (a == 0):
        return b
    if (b == 0):
        return a
  
    if (a == b):
        return a
  
    if (a > b):
        return gcd(a-b, b)
    return gcd(a, b-a)

def SuperGCD(n):
    ans = 0

    for i in range(1,n+1):
        ans = ans + gcd(i,n)*2**i
    
    return ans
    
n = int(input())

    
    
