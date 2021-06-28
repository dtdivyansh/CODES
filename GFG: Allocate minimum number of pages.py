def findPages(self,arr, n, m):
        if(n<m):
            return -1
        def valid(arr,x,mid):
            stu = 1
            s = 0
            for i in arr:
                s = s+i
                if(s>mid):
                    s = i
                    stu+=1
                if(stu>x):
                    return False
            return True
            
        mini = max(arr)
        maxi = sum(arr)
        res = -1
        while(mini<=maxi):
            mid = (mini+maxi)//2
            if(valid(arr,m,mid)):
                res = mid
                maxi = mid -1
            else:
                mini = mid +1
        return res
