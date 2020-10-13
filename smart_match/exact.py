class Exact():
        
    def similarity(self, s, t):
        return 1.0 if s == t else 0.0
    
    def dissimilarity(self, s, t):
        return 1 - self.similarity(s, t)
    
    def __repr__(self):
        return 'Exact'