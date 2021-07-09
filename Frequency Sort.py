import heapq as hq

def frequencySort(arr):
    dic = {}

    for i in arr:
        if(i in dic.keys()):
            dic[i]+=1
        else:
            dic[i]=1

    heap = []
    
    for i in arr:
        hq.heappush(heap,(-1*dic[i],i))
        
    ans = []
    while(heap):
        val = hq.heappop(heap)
        ans.append(val[1])
    return ans

arr = list( map( int, input().split() ) )

ans = frequencySort(arr)

print(ans)