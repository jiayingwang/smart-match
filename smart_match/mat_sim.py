class MatSim:
    
    def __init__(self, start_gap=1, gap=1, mismatch=1, match=0, transpose=1, opt=min, allow_transpose=False):
        self.start_gap = start_gap
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
    
    def dp_sw(self, s, t):
        if not s:
            return len(t) * self.gap
        if not t:
            return len(s) * self.gap
        if s == t:
            return len(s) * self.match
        
        matrix = [[0 for i in range(len(t)+1)] for j in range(len(s)+1)]
        max_cost = 0
            
        for i in range(len(s)):
            for j in range(len(t)):
                gap_cost = 0
                for k in range(i+1):
                    gap_cost = max(gap_cost, matrix[i-k][j+1] + self.start_gap + self.gap * k)
                
                for k in range(j+1):
                    gap_cost = max(gap_cost, matrix[i+1][j-k] + self.start_gap + self.gap * k)
                    
                matrix[i+1][j+1] = max(0, gap_cost, matrix[i][j] + (self.match if s[i] == t[j] else self.mismatch))
                max_cost = max(max_cost, matrix[i+1][j+1])
            
        return max_cost
    
    def dp_local(self, s, t):
        if not s:
            return len(t) * self.gap
        if not t:
            return len(s) * self.gap
        if s == t:
            return len(s) * self.match
        
        row1 = [0]*(len(t)+1)
        row2 = [0]*(len(t)+1)
        
        for i in range(len(t)+1):
            row1[i] = 0
            
        for i in range(len(s)):
            row2[0] = 0
            for j in range(len(t)):
                row2[j+1] = self.opt(0, row2[j] + self.gap,
                                    row1[j+1] + self.gap,
                                    row1[j] + (self.match if s[i] == t[j] else self.mismatch))
            row1, row2 = row2, row1
            
        return row1[len(t)]
    
    def lc_substring(self, s, t):
        '''
            longest common substring
        '''
        row1 = [0]*(len(t)+1)
        row2 = [0]*(len(t)+1)
        
        max_len = 0
            
        for i in range(len(s)):
            row2[0] = 0
            for j in range(len(t)):
                if s[i] == t[j]:
                    row2[j+1] = row1[j] + 1
                    if row2[j+1] > max_len:
                        max_len = row2[j+1]
            row1, row2 = row2, [0]*(len(t)+1)
            
        return max_len
    
    def lc_subsequence(self, s, t):
        '''
            longest common substring
        '''
        row1 = [0]*(len(t)+1)
        row2 = [0]*(len(t)+1)
        
        max_len = 0
            
        for i in range(len(s)):
            row2[0] = 0
            for j in range(len(t)):
                if s[i] == t[j]:
                    row2[j+1] = row1[j] + 1
                else:
                    row2[j+1] = max(row2[j], row1[j+1])
            row1, row2 = row2, row1
            
        return row1[len(t)]
