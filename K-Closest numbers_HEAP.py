import heapq

def closestNumbers(arr,x,k):
    heap = []
    size = 0
    for i in arr:
        ab = abs(x-i)
        heapq.heappush(heap, (-1*ab,i))
        size+=1
        if(size>k):
            heapq.heappop(heap)
            size-=1
            
    ans = [j for i,j in heap]
    return ans
    
arr = list(map(int,input().split()))
x = int(input())
k = int(input())

'''
arr = [5,6,7,8,9]
x = 7
k = 3
'''

ans = closestNumbers(arr, x, k)
print(ans)