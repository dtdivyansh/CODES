count = 0
for _ in range( int( input() ) ):
    n = int(input())
    arr = [int(i) for i in input().split()]
    limit = n*(n-1)//2 - 1
    if( arr == sorted(arr) ):
        print("YES")
    else:
        def mergeSort(arr,l,r):
           global count  
           if l < r:
               # getting the average
               m = (l+(r-1))//2
               # Sort
               mergeSort(arr, l, m)
               mergeSort(arr, m+1, r)
               merge(arr, l, m, r)
              
        def merge(arr, l, m, r):
            global count
            n1 = m - l + 1
            n2 = r- m
            # create arrays
            L = [0] * (n1)
            R = [0] * (n2)
            # Copy data to arrays
            for i in range(0 , n1):
                L[i] = arr[l + i]
            for j in range(0 , n2):
                R[j] = arr[m + 1 + j]
            i = 0 # first half of array
            j = 0 # second half of array
            k = l # merges two halves
            while i < n1 and j < n2 :
                if L[i] <= R[j]:
                    count+=1
                    arr[k] = L[i]
                    i += 1
                else:
                    count+=1
                    arr[k] = R[j]
                    j += 1
                k += 1
           # copy the left out elements of left half
            while i < n1:
               arr[k] = L[i]
               i += 1
               k += 1
           # copy the left out elements of right half
            while j < n2:
               arr[k] = R[j]
               j += 1
               k += 1
        
        mergeSort(arr,0,n-1)
        if(count>=limit):
            print("NO")
        else:
            print("YES")

