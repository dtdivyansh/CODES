	def count(self,arr, n, x):
		    i,j = 0,n-1
        ans = n
        res = -1
        while(i<=j):
            mid = i + (j-i)//2
            if(arr[mid]==x):
                ans = min(ans,mid)
                j = mid-1
            elif(arr[mid]>x):
                j = mid-1
            else:
                i = mid+1
        i=0
        j=n-1
        while(i<=j):
            mid = i + (j-i)//2
            if(arr[mid]==x):
                res = max(res,mid)
                i = mid+1
            elif(arr[mid]>x):
                j = mid-1
            else:
                i = mid+1
            
        if(ans==n):
            return 0
        else:
            return res-ans+1
