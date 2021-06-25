def findFloor(A,N,X):
        ans,val = -1,-1
        i,j=0,N-1
        while(i<=j):
            mid = (i+j)//2
            if(A[mid]==X):
                return mid
            elif(A[mid]<X):
                if(A[mid]>val):
                    val = A[mid]
                    ans = mid
                i=mid+1
            else:
                j = mid-1
        return ans
