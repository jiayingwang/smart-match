from .mat_sim import MatSim

class NeedlemanWunch(MatSim):
    
    def __init__(self):
        super().__init__(gap=-2, mismatch=-1, match=0, opt=max)

    def similarity(self, s, t):
        if not s and not t:
            return 1.0
        if not s or not t:
            return 0.0
        max_score = max(len(s), len(t)) * self.match
        min_score = max(len(s), len(t)) * min(self.mismatch, self.gap)
        return (self.score(s, t)-min_score) / (max_score-min_score)
    
    def score(self, s, t):
        return self.dp(s, t)

    def dissimilarity(self, s, t):
        return 1 - self.similarity(s, t)

    def __repr__(self):
        return f'NeedlemanWunch [match={self.match}, mismatch={self.mismatch}, gap={self.gap}]'
