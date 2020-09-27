class JaroWinkler:
 def jaro_Winkler_distance(self,s,t):
    if len(s)>len(t):
        longerStr=s
        shorterStr=t
    else:
        longerStr=t
        shorterStr=s

    mW=(len(longerStr)//2)-1

    shortMached=[]
    longerMached=[]
    matches=0

    for i,char in enumerate(shorterStr):
        for j in range(max(0,i-mW),min(len(longerStr),i+mW+1)):
            if char==longerStr[j]:
                matches=matches+1
                shortMached.append(char)
                longerMached.insert(j,char)
                break

    halfTrans=0
    p = 0.1
    pF = 0
    for m in range(0,len(shortMached)):

        if(shortMached[m]!=longerMached[m]):
            halfTrans=halfTrans+1

        elif (shortMached[m]==longerMached[m]):
            pF = pF + 1

    simJaro=((matches/len(s))+(matches/len(t))+(matches-(halfTrans//2))/matches)/3
    return simJaro + pF*p*(1-simJaro)

 def __repr__(self):
     return JaroWinkler
