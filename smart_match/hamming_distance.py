class HammingDistance:
     
    def similarity(self, s, t):
        return 1 - self.dissimilarity(s, t)
    
    def dissimilarity(self, s, t):
        if not s and not t:
            return 0
        return self.distance(s, t) / max(len(s), len(t))

    def distance(self, s, t):
        assert len(s) == len(t), 'undefined for sequences of unequal length'
        
        if not s:
            return 0
        
        distance = 0
        for s1,t1 in zip(s, t):
            if(s1 != t1):
                distance += 1
        return distance
    
    def _repr_(self):
        return 'HammingDistance'