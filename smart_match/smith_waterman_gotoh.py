from .mat_sim import MatSim

class SmithWatermanGotoh(MatSim):
    
    def __init__(self):
        super().__init__(gap=-0.5, mismatch=-2, match=1, opt=max)

    def similarity(self, s, t):
        if not s and not t:
            return 1.0
        if not s or not t:
            return 0.0
        max_score = min(len(s), len(t)) * self.match
        return self.score(s, t) / max_score
    
    def score(self, s, t):
        return self.dp_local(s, t)

    def dissimilarity(self, s, t):
        return 1 - self.similarity(s, t)

    def __repr__(self):
        return f'SmithWatermanGotoh [match={self.match}, mismatch={self.mismatch}, gap={self.gap}]'
