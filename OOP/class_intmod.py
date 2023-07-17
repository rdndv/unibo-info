class IntMod:
    # la tua init QUI
    def __init__(self,i,m):
        if type(i)!= int or type(m)!=int:
            raise TypeError
        if m<=0:
            raise ValueError
        self.__i = i
        self.__m = m
        self.__im = self.__i%self.__m
        
    def set_m (self,other_m):
        self.__m = other_m
        self.__im = self.__i%self.__m
        return self
    
    def __add__(self,other):
        if isinstance(other,IntMod):
            if self.__m == other.__m:
                somma = self.__i + other.__i
                return IntMod(somma,self.__m)
            raise ValueError("Moduli Diversi")
        else:
            try:
                other = int(other)
                somma = self.__i + other
                return IntMod(somma,self.__m)
            except:
                raise TypeError("Non Intero")
    def get(self):
        return self.__i
    
    def __str__(self): 
        return str(self.__im)+" (mod "+str(self.__m)+")"


class IntMod2(IntMod):
    def __init__(self,i):
        super().__init__(i,2)
    
    def set_m (self,other_m):
        raise TypeError("Impossibile cambiare modulo")
    
    def __add__(self,other):
        r = super().__add__(other)
        return IntMod2(r.get())
