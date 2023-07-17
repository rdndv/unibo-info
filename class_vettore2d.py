from math import *
class Vettore2D:
    
    def __init__(self,x,y):
        self.__x = float(x)
        self.__y = float(y)
        
    def __sub__(self,other):
        return Vettore2D(self.__x - other.__x, self.__y - other.__y)
    
    def __mul__(self,other):
        if type(other)== int or type(other)== float:            
            return Vettore2D(self.__x*other, self.__y*other)
        raise NotImplementedError
    
    def __abs__(self):
        return sqrt(self.__x**2 + self.__y**2)
    
    def distanza_da(self,other):
        return self.__abs__() - other.__abs__()
      

    def __str__(self): #data, non modificare
        return 'OA = ('+str(self.__x)+', '+str(self.__y)+')'
    
print(round(Vettore2D(3, 4).distanza_da(Vettore2D(1, 2)),1))
