def longestUniqueSubsttr(S):
        size = len(S)
        head = 0
        tail = 1
        m = 0
        while(tail<size):
            stri = S[head:tail]
            #print('STRING: ',stri,S[tail])
            if(S[tail] not in stri):
                #print(head,tail,stri,S[tail])
                l = len(S[head:tail+1])
                tail+=1
                if(l>m and l>2):
                    #print('sel ',S[head:tail])
                    m = l
            else:
                ind = stri.index(S[tail]) + len(S[0:head])
                head = ind+1
                tail+=1
        if(m==0):
            return -1
        return m
    
stri = 'gefgees'
print(longestUniqueSubsttr(stri))
