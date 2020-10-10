from collections import Counter
from math import sqrt

class EuclideanDistance:
        
    def similarity(self, s, t):       
        return 1 - self.dissimilarity(s, t)
    
    def dissimilarity(self, s, t):
        if not s and not t:
            return 0.0
        max_distance = sqrt(len(s)**2 + len(t)**2)
        return self.distance(s, t) / max_distance
    
    def distance(self, s, t):
        s_freq = Counter(s)
        t_freq = Counter(t)
        s_t_diff = s_freq - t_freq
        t_s_diff = t_freq - s_freq
        distance = 0
        diff = s_t_diff + t_s_diff
        for x in diff:
            distance += diff[x] ** 2
            
        return sqrt(distance)
    
    def __repr__(self):
        return 'EuclideanDistance'
