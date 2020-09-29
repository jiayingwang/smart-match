import numpy as np
class SmithWatermanGotoh():

    def Similarity(self,s,t):
        matchValue=1
        if not s and not t:
            return 1
        if not s or not t:
            return 0
        maxDistance = min(len(s),len(t))*matchValue
        return self.Scroe_metrix(s,t)/maxDistance

    def dissimilarity(self,s,t):
        return 1 - self.Similarity(s,t)

    def compare(self,s, i, t, j):
        matchValue = 1
        misMatchValue = -2
        if (s[i] == t[j]):
            return matchValue
        if (s[i] != t[j]):
            return misMatchValue

    def Scroe_metrix(self,s,t):
        GapValue = -0.5
        metrix = np.zeros([len(s), len(t)])
        metrix[0, 0] = max(0, GapValue, self.compare(s, 0, t, 0))
        for i in range(1, len(s)):
            metrix[i, 0] = max(0, metrix[i - 1, 0] + GapValue, self.compare(s, i, t, 0))
        for i in range(1, len(t)):
            metrix[0, i] = max(0, metrix[0, i - 1] + GapValue, self.compare(s, 0, t, i))
        for i in range(1, len(s)):
            for j in range(1, len(t)):
                metrix[i,j] = max(0, metrix[i, j - 1] + GapValue, metrix[i - 1, j] + GapValue,
                         metrix[i - 1, j - 1] + self.compare(s, i, t, j))
        return metrix.max()

    def __repr__(self):
        return 'SmithWatermanGotoh'
