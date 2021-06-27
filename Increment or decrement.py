def check(self, N, A, X): 
        A[0]+=X
        for i in range(1,N):
            if(A[i]>=A[i-1]):
                A[i]-=X
                if(A[i]>=A[i-1]):
                    return False
            else:
                if(A[i]+X < A[i-1]):
                    A[i]+=X
        return True
