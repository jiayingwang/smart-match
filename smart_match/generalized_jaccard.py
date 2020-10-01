from collections import Counter

class GeneralizedJaccard:
        
    def similarity(self, s, t):
        if not s and not t:
            return 1
        
        if not s or not t:
            return 0
        
        s_freq = Counter(s)
        t_freq = Counter(t)
        
        intersection = s_freq & t_freq
        intersection_size = sum(intersection.values())
                
        return intersection_size / (len(s) + len(t) - intersection_size)
    
    def dissimilarity(self, s, t):
        return 1 - self.similarity(s, t)
    
    def __repr__(self):
        return 'GeneralizedJaccard'
