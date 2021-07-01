import heapq as hpq

arr = [int(i) for i in input().split()]
k  = int(input())+1
heap = []
c = 0
size=0
#ans = []

for i in range(len(arr)):
    if(size<k):
        hpq.heappush(heap, arr[i])
        size+=1
    else:
        v = hpq.heappop(heap)
        arr[c]=v
        c+=1
        hpq.heappush(heap, arr[i])
   
while(heap):
    v = hpq.heappop(heap)
    arr[c]=v
    c+=1
 
print(arr)
