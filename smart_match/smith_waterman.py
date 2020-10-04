from .mat_sim import MatSim

class SmithWaterman(MatSim):
    
    def __init__(self):
        super().__init__(start_gap=-5, gap=-1, mismatch=-3, match=5, opt=max)
        
    def set_params(self, start_gap=None, gap=None, mismatch=None, match=None):
        if start_gap:
            self.start_gap = start_gap
        if gap:
            self.gap = gap
        if mismatch:
            self.mismatch = mismatch
        if match:
            self.match = match

    def similarity(self, s, t):
        if not s and not t:
            return 1.0
        if not s or not t:
            return 0.0
        max_score = min(len(s), len(t)) * self.match
        return self.score(s, t) / max_score
    
    def score(self, s, t):
        return self.dp_sw(s, t)

    def dissimilarity(self, s, t):
        return 1 - self.similarity(s, t)

    def __repr__(self):
        return f'SmithWaterman [match={self.match}, mismatch={self.mismatch}, start_gap={self.start_gap}, gap={self.gap}]'
