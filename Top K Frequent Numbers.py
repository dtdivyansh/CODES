import heapq as hq

arr = list(map( int,input().split() ))
k = int(input())
dic = {}

for i in arr:
    if(i in dic.keys()):
        dic[i]+=1
    else:
        dic[i]=1

s = set(arr)
heap = []
size=0

for i in s:
    hq.heappush(heap,(dic[i],i))
    size+=1
    if(size>k):
        hq.heappop(heap)
        size-=1

print(heap)
    
    