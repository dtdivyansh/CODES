def pair(arr,n):
    dic = {}
    for num in arr:
        s = 0
        while(num>0):
            s+=(num%10)
            num=num//10
        if(s not in dic.keys()):
            dic[s] = 1
        else:
            dic[s]+=1
    
    li = dic.values()
    total = 0
    for num in li:
        total = total+ num*(num-1)//2
    return total

arr = [44,17,3212,53,8]
n = len(arr)

val = pair(arr, n)

print(val)