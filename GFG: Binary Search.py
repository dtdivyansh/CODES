def searchInSorted(self,arr, N, K):
        i=0
        j=N
        while(i<=j):
            mid= i + (j-i)//2
            if(arr[mid]==K):
                return 1
            elif(arr[mid]>K):
                j = mid-1
            else:
                i = mid+1
        return -1
        
