from .mat_sim import MatSim

class SmithWatermanGotoh(MatSim):
    
    def __init__(self):
        super().__init__(gap=-0.5, mismatch=-2, match=1, opt=max)
        
    def set_params(self, gap=None, mismatch=None, match=None):
        if gap:
            self.gap = gap
        if mismatch:
            self.mismatch = mismatch
        if match:
            self.match = match

    def similarity(self,s,t):
        if not s and not t:
            return 1
        if not s or not t:
            return 0
        max_score = min(len(s), len(t)) * self.match
        return self.dp_local(s, t) / max_score

    def dissimilarity(self, s, t):
        return 1 - self.similarity(s, t)

    def __repr__(self):
        return f'SmithWatermanGotoh [match={self.match}, mismatch={self.mismatch}, gap={self.gap}]'
