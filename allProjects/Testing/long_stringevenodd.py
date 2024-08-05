


def longest_substring(lstring):
    lss=""
    for i in range(0,len(lstring)-1):
        firstj=1
        lastslicei=i
        for j in range(i,len(lstring)):
            
            if firstj ==1:
                curreo=int(lstring[j])%2
                lasteo=curreo
                firstj+=1

            else:
                curreo=int(lstring[j])%2
                if curreo != lasteo:
                    lastslicei=j
                    lasteo=curreo
                else:
                    break

        if lastslicei > i and len(lss) < lastslicei +1 - i:
            lss=lstring[i:lastslicei+1]   

    if lss:
        print (lss)
    else:
        print("no match found")      


longest_substring("225424272163254474441338664823")   
longest_substring("594127169973391692147228678476")
longest_substring("721449827599186159274227324466")   
longest_substring("777777777777777223322352233222")     





   

            


