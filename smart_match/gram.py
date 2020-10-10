class Gram:
  
    def __init__(self, q=2, mode='default', space='_', in_term_only=True):
        self.q = q
        self.mode = mode
        self.space = space
        self.in_term_only = in_term_only
        
    def set_params(self, q=None, mode=None, space=None, in_term_only=None):
        if q:
            self.q = q
        if mode:
            self.mode = mode
        if space:
            self.space = space
        if in_term_only:
            self.in_term_only = in_term_only
        else:
            raise NotImplementedError

    def get_grams(self, x):
        if self.mode == 'symmetry':
            space = self.space*(self.q-1)
            x = space + x + space
        elif self.mode == 'equal':
            x = '_' + x + space
        G = []
        for i in range(len(x)-self.q+1):
            G.append(x[i:i+self.q])
        return G
    
    def grams(self, x):
        if self.in_term_only:
            G = []
            terms = x.split()
            for term in terms:
                G += self.get_grams(term)
            return G
        else:
            return self.get_grams(x)
      
    def __repr__(self):
        return f"Gram[q={self.q}]"