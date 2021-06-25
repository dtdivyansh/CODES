def matSearch(self,mat, N, M, X):
		i,j = 0,N-1
		row=5
		mid= -1
		while(i<=j):
		    if(N==1):
		        break
		    mid = (i+j)//2
		    if(mat[mid][0]==X):
		        row=mid
		        break
		    if(mid==N-1 and mat[mid-1][0]<X):
		        row=mid
		        break
		    if(mat[mid+1][0]>X and mat[mid][0]<X):
		        row=mid
		        break
		    if(mat[mid][0]>X):
		        j = mid-1
		    else:
		        i = mid+1
		row=mid      
		i,j=0,M-1
		while(i<=j):
	       mid = (i+j)//2
		   if(mat[row][mid]==X):
		       return 1
		   if(mat[row][mid]>X):
		       j = mid-1
		   else:
		       i=mid+1
		return 0
