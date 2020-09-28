class Jaro:
    
    def similarity(self, s, t):
        if not s and not t:
            return 1
        
        if not s or not t:
            return 0
        
        if len(s) > len(t):
            s, t = t, s

        max_dist = (len(t) // 2) - 1

        s_matched = []
        t_matched = []
        matches = 0

        for i, c in enumerate(s):
            for j in range(max(0, i-max_dist), min(len(t), i+max_dist+1)):
                if c == t[j]:
                    matches += 1
                    s_matched.append(c)
                    t_matched.insert(j, c)
                    break
        
        transpositions = 0
        for m in range(0, len(s_matched)):
            if(s_matched[m] != t_matched[m]):
                transpositions += 1

        return  (matches/len(s) + matches / len(t) + (matches-(transpositions//2)) / matches) / 3
    
    def dissimilarity(self, s, t):
        return 1 - self.similarity(s, t)
    
    def __repr__(self):
        return 'Jaro'