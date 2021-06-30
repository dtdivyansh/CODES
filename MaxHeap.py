import heapq

q = []
arr = [(1,7),(2,5),(4,3)]

for i in arr:
    heapq.heappush(q, (-1*i[1],i))

        
print([i[1] for i in q])
