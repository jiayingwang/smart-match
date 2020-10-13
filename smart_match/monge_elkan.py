import smart_match
from math import sqrt

class MongeElkan:
    
    def __init__(self):
        self.method = smart_match.get_method()
        
    def set_params(self, method=None):
        if method:
            self.method = smart_match.get_method(method)
    
    def similarity(self, X, Y):
        if not X and not Y:
            return 1.0
        
        if not X or not Y:
            return 0.0

        return sqrt(self.monge_elkan(X, Y) * self.monge_elkan(Y, X))
    
    def monge_elkan(self, s, t):
        sum_score = 0
        
        for x in s:
            max_score = 0
            for y in t:
                max_score = max(max_score, self.method.similarity(x, y))
            sum_score += max_score
            
        return sum_score / len(s)
                
    
    def dissimilarity(self, s, t):
        return 1 - self.similarity(s, t)        
    
    def __repr__(self):
        return f'MongeElkan [method={self.method}]'