from collections import Counter

class BlockDistance():
        
    def similarity(self, s, t):
        return 1 - self.dissimilarity(s, t)
    
    def dissimilarity(self, s, t):
        if not s and not t:
            return 0.0
        return self.distance(s, t) / (len(s) + len(t))
    
    def distance(self, s, t):
        distance = 0
        s_freq = Counter(s)
        t_freq = Counter(t)
        s_freq.subtract(t_freq)
        total = 0
        for x in s_freq:
            total += abs(s_freq[x])
        return total
    
    def __repr__(self):
        return 'BlockDistance'
