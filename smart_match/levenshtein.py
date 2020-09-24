from .mat_sim import MatSim

class Levenshtein(MatSim):
    
    def __init__(self):
        super().__init__()
    
    def similarity(self, s, t):
        return 1 - self.dissimilarity(s, t)
    
    def dissimilarity(self, s, t):
        if not s and not t:
            return 0
        return self.distance(s, t) / max(len(s), len(t)) 
    
    def distance(self, s, t):
        return self.dp(s, t)
    
    def __repr__(self):
        return f'Levenshtein [match={self.match}, mismatch={self.mismatch}, gap={self.gap}]'