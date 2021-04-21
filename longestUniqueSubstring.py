s = input()
s = s.lower()

dic = {}
m = ''
c=0
for i in s:
    if( i not in dic.keys() ):
        dic[i]=1
        c+=1
    else:
        if(c>len(m)):
            m= ''.join(dic.keys())
        c=0
        dic = {}
        
if(len(m)>=3):
    print(m)
else:
    print(-1)
