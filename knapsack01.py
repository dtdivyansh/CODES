def knapsack(w,v,m,n):
    if(n==0 or m==0):
        return 0
    elif(w[n-1]<=m):
        return max(v[n-1] + knapsack(w,v,m-w[n-1],n-1) , knapsack(w,v,m,n-1))
    return knapsack(w, v, m, n-1)


def wtMatrix(w,v,m,n):
    mat = []
    for i in range(n+1):
        mat.append([])
        for j in range(m+1):
            if(i==0 or j==0):
                mat[i].append(0)
            elif(w[i]<=m):
                if(j-w[i]<0):
                    mat[i].append(mat[i-1][j]) 
                else:
                    mat[i].append(max( mat[i-1][j] , mat[i-1][j-w[i]] + v[i] ))
            else:
                mat[i].append(mat[i-1][j]) 
                
    sel = []
    i=n
    j=m
    while(i>0):
        if(j==0):
            sel.insert(0,0)
            
        elif(mat[i][j]!=mat[i-1][j]):
            sel.insert(0,1)
            j=j-w[i]
        else:
            sel.insert(0,0)
        i-=1
    print(sel)                
    return mat[n][m]
        
    #for i in range(n+1):
     #   for j in range(m+1):
      #      print(mat[i][j],end=",")
       # print()


n = int(input("Enter number of objects: "))
w = [int(i) for i in input("input weights of objects: ").split()]
v = [int(i) for i in input("input their values respectively: ").split()]
m = int(input("Enter Max value of Knapsack: "))
print(w)
print(v)
profit = knapsack(w, v, m, n)
print(profit)
w.insert(0,0)
v.insert(0,0)
profit2 = wtMatrix(w,v,m,n)
print(profit2)