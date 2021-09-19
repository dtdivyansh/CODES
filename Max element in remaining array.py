n = int(input())
arr = []
maxi = 0
sec = 0
for i in range(n):
    arr.append( int(input()) )
    if(arr[i]>=arr[maxi]):
        sec = maxi
        maxi = i
    else:
        if(arr[i]>arr[sec]):
            sec = i
        elif(maxi==sec and arr[i]<arr[sec]):
            sec = i
            
for i in range(n):
    if(i==maxi):
        print(arr[sec])
    else:
        print(arr[maxi])
