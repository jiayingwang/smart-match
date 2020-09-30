import numpy as np
class SmithWaterman():

    def Similarity(self,s,t):
        matchValue=5
        if not s and not t:
            return 1
        if not s or not t:
            return 0
        maxDistance = min(len(s),len(t))*matchValue
        return self.Scroe_metrix(s,t)/maxDistance

    def dissimilarity(self,s,t):
        return 1 - self.Similarity(s,t)

    def compare(self,s, i, t, j):
        matchValue = 5
        misMatchValue = -3
        if (s[i] == t[j]):
            return matchValue
        if (s[i] != t[j]):
            return misMatchValue

    def Scroe_metrix(self,s,t):
        GapValue = -5
        metrix = np.zeros([len(s)+1, len(t)+1])
        for i in range(len(s)):
            metrix[i, 0] = 0
        for i in range(len(t)):
            metrix[0, i] = 0
        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                metrix[i,j] = max(0, metrix[i, j - 1] + GapValue, metrix[i - 1, j] + GapValue,
                         metrix[i - 1, j - 1] + self.compare(s, i-1, t, j-1))
        return metrix.max()

    def __repr__(self):
        return 'SmithWaterman'
