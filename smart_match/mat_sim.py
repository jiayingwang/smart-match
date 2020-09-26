class MatSim:
    
    def __init__(self, gap=1, mismatch=1, match=0, transpose=1, opt=min, allow_transpose=False):
        self.gap = gap
        self.mismatch = mismatch
        self.match = match
        self.transpose = transpose
        self.opt = opt
        self.allow_transpose = allow_transpose
    
    def dp(self, s, t):
        if not s:
            return len(t) * self.gap
        if not t:
            return len(s) * self.gap
        if s == t:
            return len(s) * self.match
        
        row1 = [0]*(len(t)+1)
        row2 = [0]*(len(t)+1)
        if self.allow_transpose:
            row3 = [0]*(len(t)+1)
        for i in range(len(t)+1):
            row1[i] = i * self.gap
            
        for i in range(len(s)):
            row2[0] = (i+1) * self.gap
            for j in range(len(t)):
                row2[j+1] = self.opt(row2[j] + self.gap,
                                    row1[j+1] + self.gap,
                                    row1[j] + (self.match if s[i] == t[j] else self.mismatch)) 
                if self.allow_transpose and i > 0 and j > 0 and s[i-1] == t[j] and s[i] == t[j-1]:
                    row2[j+1] = self.opt(row2[j+1], row3[j-1]+self.transpose)
            if self.allow_transpose:
                row1, row2, row3 = row2, row3, row1
            else:
                row1, row2 = row2, row1
            
        return row1[len(t)]
