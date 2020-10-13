from math import sqrt
from collections import Counter

class CosineSimilarity():
    """
        Cosine Similarity
    """
    
    def similarity(self, s, t):
        if not s and not t:
            return 1.0
        
        if not s or not t:
            return 0.0
        
        dot_product = 0
        S2 = 0
        T2 = 0
        s_freq = Counter(s)
        t_freq = Counter(t)
        
        for x in set(s_freq + t_freq):
            dot_product += s_freq[x] * t_freq[x]
            S2 += s_freq[x] ** 2
            T2 += t_freq[x] ** 2           
        return dot_product / (sqrt(S2) * sqrt(T2))
    
    def dissimilarity(self, s, t):
        return 1 - self.similarity(s, t)
    
    def __repr__(self):
        return 'CosineSimilarity'
