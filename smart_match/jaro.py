class Jaro:
    
    def similarity(self, s, t):
        if not s and not t:
            return 1.0
        
        if not s or not t:
            return 0.0

        max_dist = (max(len(s), len(t)) // 2) - 1

        matches = 0
        hash_s = [0] * len(s) 
        hash_t = [0] * len(t) 

        for i, c in enumerate(s):
            for j in range(max(0, i-max_dist), min(len(t), i+max_dist+1)):
                if c == t[j] and hash_t[j] == 0:
                    matches += 1
                    hash_s[i] = 1
                    hash_t[j] = 1
                    break
        
        transpositions = 0
        j = 0
        for i in range(0, len(s)):
            if hash_s[i]:
                while hash_t[j] == 0:
                    j += 1
                if s[i] != t[j]:
                    transpositions += 1
                j += 1
        if matches == 0:
            return 0.0
        return  (matches/len(s) + matches / len(t) + (matches-(transpositions/2)) / matches) / 3
    
    def dissimilarity(self, s, t):
        return 1 - self.similarity(s, t)
    
    def __repr__(self):
        return 'Jaro'