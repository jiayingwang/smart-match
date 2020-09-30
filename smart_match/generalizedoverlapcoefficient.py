from multiset import *      #需要pip install multiset

class GeOverlapCoefficient:

    def intersection(self,s,t):
        x = Multiset(s)
        y = Multiset(t)
        if len(x) < len(y):
            return Multiset.intersection(x,y)
        
        return Multiset.intersection(y,x)
        
    def similarity(self,s,t):
        
        if not s and not t:
            return 1.0

        if not s or not t:
            return 0.0
        
        return len(self.intersection(s,t)) / min(len(s),len(t))
    
    def distance(self,s,t):

        return 1 - self.similarity(s,t)

    def dissimilarity(self,s,t):

        return 1 - self.similarity(s,t)

