import heapq

q = []
arr = [7,10,5,20,11,3]
n = 2
size=0
for i in arr:
    heapq.heappush(q, i)
    size+=1
    if(size>n):
        heapq.heappop(q)
        size-=1
        
print(q[0])
