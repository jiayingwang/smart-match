from smart_match.mat_sim import MatSim

class LongestCommonSubstring(MatSim):
        
    def similarity(self, s, t):
        if not s and not t:
            return 1.0
        if not s or not t:
            return 0.0
        return self.lcs(s, t) / max(len(s), len(t)) 
            
    def dissimilarity(self, s, t):
        return 1 - self.similarity(s, t)
    
    def distance(self, s, t):
        return len(s) + len(t) - 2*self.score(s, t)
    
    def score(self, s, t):
        return self.lcs(s, t)
    
    def __repr__(self):
        return 'LongestCommonSubstring'