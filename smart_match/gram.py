class Gram:
  
    def __init__(self, q=2, mode='default', space='_'):
        self.q = q
        self.mode = mode
        self.space = space
        
    def set_params(self, q=None, mode=None, space=None):
        if q:
            self.q = q
        if mode:
            self.mode = mode
        if space:
            self.space = space

    def grams(self, x):
        if self.mode == 'symmetry':
            space = self.space*(self.q-1)
            x = space + x + space
        elif self.mode == 'equal':
            x = '_' + x + space
        G = []
        for i in range(len(x)-self.q+1):
            G.append(x[i:i+self.q])
        return G
      
    def __repr__(self):
        return f"Gram[q={self.q}]"