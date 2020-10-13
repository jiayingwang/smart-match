class DiceSimilarity:
    
    def similarity(self, s, t):
        if not s and not t:
            return 1.0
        
        if not s or not t:
            return 0.0

        s_set = set(s)
        t_set = set(t)
        intersect_set = s_set.intersection(t_set) 
        
        return 2 * len(intersect_set) / (len(s_set) + len(t_set))
    
    def dissimilarity(self, s, t):
        return 1 - self.similarity(s, t)        
    
    def __repr__(self):
        return 'Dice'