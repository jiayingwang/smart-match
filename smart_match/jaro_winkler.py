from .jaro import Jaro

class JaroWinkler:
    
    def __init__(self, boost_threshold=0.7, prefix_scale=0.1, max_prefix_length=4):
        self.boost_threshold = boost_threshold
        self.prefix_scale = prefix_scale
        self.max_prefix_length = max_prefix_length
        self.jaro = Jaro()
        
    def set_params(self, boost_threshold=None, prefix_scale=None, max_prefix_length=None):
        if boost_threshold:
            self.boost_threshold = boost_threshold
        if prefix_scale:
            self.prefix_scale = prefix_scale
        if max_prefix_length:
            self.max_prefix_length = max_prefix_length
    
    def similarity(self, s, t):
        jaro_similarity = self.jaro.similarity(s, t)
        if jaro_similarity > self.boost_threshold:
            prefix = 0
            for i in range(min(len(s), len(t))):
                if s[i] == t[i]:
                    prefix += 1
                else:
                    break
            prefix = min(self.max_prefix_length, prefix)

            jaro_similarity += self.prefix_scale * prefix * (1 - jaro_similarity)
        
        return jaro_similarity
    
    def dissimilarity(self, s, t):
        return 1 - self.similarity(s, t)
    
    def __repr__(self):
        return f"JaroWinkler [boost_threshold:{self.boost_threshold}, prefix_scale: {self.prefix_scale}, max_prefix_length:{self.max_prefix_length}]"