maxArr = []
arr = [ int(i) for i in input().split()]
k = int(input())

def push2(i):
    global arr
    if not maxArr:
        maxArr.append([arr[i],i])
        return 0
    else:
        while maxArr:
            if( maxArr[-1][0] < arr[i] ):
                maxArr.pop(-1)
            else:
                break
        maxArr.append([arr[i],i])


def maxFind(head):
    while( maxArr[0][1] < head ):
        maxArr.pop(0)
    return maxArr[0][0]


head = 0
tail = k
for i in range(k):
    push2(i)
    
print( maxFind(head),end=" " )

while(tail<len(arr)):
    head+=1
    push2(tail)
    print( maxFind(head),end=" " )
    tail+=1
    