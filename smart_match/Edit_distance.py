import numpy.matlib as np

class similarity_join():
    def __init__(self,string1,string2):
        self.string1=str(string1)
        self.string2=str(string2)
        a=len(self.string1)+1
        b=len(self.string2)+1
        self.matrix=np.zeros([a,b],dtype=int)
        for i in np.arange(len(self.string2)+1):
           self.matrix[0,i]=i
        for j in np.arange(len(self.string1)+1):
           self.matrix[j,0]=j
    def edit_distance(self):
       for i in np.arange(1,len(self.string1)+1):
           for j in np.arange(1,len(self.string2)+1):
               if self.string1[i-1]==self.string2[j-1]:
                   self.matrix[i,j]=self.matrix[i-1,j-1]
               else:
                   deletion = self.matrix[i-1,j] + 1
                   insertion = self.matrix[i,j-1] + 1
                   substitution =self.matrix[i-1,j-1] +1
                   self.matrix[i,j]=min(deletion,insertion,substitution)
       print(self.matrix)
ls=similarity_join("member","atmosphere")
ls.edit_distance()
