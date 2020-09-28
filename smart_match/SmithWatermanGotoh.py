class SmithWatermanGotoh():

    def compare(self,s, i, t, j):
        matchValue = 1
        misMatchValue = -2
        if (s[i] == t[j]):
            return matchValue
        if (s[i] != t[j]):
            return misMatchValue
    def distance(self,s,t):
        matchValue=1
        if not s and not t:
            return 1
        if not s or not t:
            return 0
        maxDistance = min(len(s),len(t))*matchValue
        return self.smith_watermanGotoh(s,t)/maxDistance
    def smith_watermanGotoh(self,s,t):
        misMatchValue = -2
        GapValue = -0.5
        v0 = [0]*len(t)
        v1 = [0]*len(t)
        v0[0] =maxScore = max(0,GapValue,self.compare(s,0,t,0))
        for j in range(1,len(v0)):
            v0[j] = max(0,v0[j-1]+GapValue,self.compare(s,0,t,j))
            maxScore = max(maxScore,v0[j])
        for i in range(1,len(s)):
            GapValue = -0.5
            v1[0] = max(0,v0[0]+GapValue,self.compare(s,i,t,0))
            maxScore = max(maxScore,v1[0])
            for j in range(1,len(v0)):
                v1[j] = max(0,v0[j]+GapValue,v1[j - 1] + GapValue,v0[j - 1] + self.compare(s, i, t, j))
                maxScore = max(maxScore,v1[j])
            for i in range(len(v0)):
                v0[i] = v1[i]
        return maxScore

    def __repr__(self):
        return 'SmithWatermanGotoh'
