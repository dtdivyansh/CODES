import heapq as hq

def closest(points,k):
    dist = lambda x,y: ( x**2 + y**2 )**(1/2)
    heap = []
    size = 0
    for x,y in points:
        d = dist(x,y)
        hq.heappush(heap,(-1*d,[x,y]))
        size+=1
        if(size>k):
            hq.heappop(heap)
            size-=1
    ans = []        
    while(heap):
        v = hq.heappop(heap)
        ans.append(v[1])
    print(ans)
    
points = [ [1,3],[-2,2],[5,8],[0,1] ]
k = 2

closest(points, k)