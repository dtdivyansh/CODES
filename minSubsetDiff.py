def minDiffSubset(arr,n,s):
    if(n<0 and s!=0):
        return False
    elif(s==0):
        return True
    elif(arr[n]<=s):
        return minDiffSubset(arr, n-1, s-arr[n]) or minDiffSubset(arr, n-1, s)
    else:
        return minDiffSubset(arr, n-1, s)
    
def getMinDiff(arr,n,s):
    m = 1000007
    for i in range(s//2+1):
        #print('sum',i)
        if( minDiffSubset(arr, n-1, i) ):
            cal = s - 2*i
            #print(cal)
            m = min(m,cal)     
    return m

arr = [1,4,2,9]
s = sum(arr)
n = len(arr)
diff = getMinDiff(arr, n, s)
print(diff) 