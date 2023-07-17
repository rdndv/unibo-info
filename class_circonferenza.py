from math import pi
class Circonferenza:
    # qui definire la init
    def __init__(self, x,y,r):        
        self.__centro = (float(x),float(y))
        if float(r)<0:
            raise ValueError
        self.__r = float(r)
        
    def lunghezza(self):
        return self.__r*2*pi
    
    def __eq__(self,other):
        if isinstance(other,Circonferenza):
            return self.__centro == other.__centro and self.__r == other.__r
        return False    

    def __str__(self): #data - non modificare
        return f"C in {self.__centro} di r. {self.__r}"

class CirconferenzaUnitaria(Circonferenza):
    def __init__(self):
        super().__init__(0,0,1)
    
    def lunghezza(self):
        return 2*pi
    
print(CirconferenzaUnitaria())

