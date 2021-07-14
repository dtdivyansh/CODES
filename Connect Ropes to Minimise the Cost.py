import heapq as hq

def ropes(arr):
    heap = []
    for i in arr:
        hq.heappush(heap,i)
        
    cost=0
    while(len(heap)>1):
        a = hq.heappop(heap)
        b = hq.heappop(heap)
        cost+=(a+b)
        hq.heappush(heap,a+b)
    
    return cost

arr = [1,2,3,4,5]

ans = ropes(arr)

print(ans)