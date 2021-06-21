class Solution:
    def findKRotation(self,arr,  n):
		i,j = 0,n-1
        ans = 100007
        res = 0
        while(i<=j):
            mid = (i+j)//2
            if(arr[mid]<ans):
                ans = arr[mid]
                res = mid
            if(arr[mid]>=arr[0] and arr[mid]<=arr[-1]):
                return 0
            if(arr[mid]>=arr[0]):
                i=mid+1
            else:
                j=mid-1
        return res
