 class HammingDistance:
 
 
    def distance(self,s,t):
        if not s:
            return 0
        if len(s)!=len(s):
            raise ValueError("undefined for sequences of unequal length")
        distance=0
        for s1,t1 in zip(s,t):
            if(s1!=t1):
                distance=distance+1
        return distance
    
    
    
    def _repr_(self):
        return 'HammingDistance'
