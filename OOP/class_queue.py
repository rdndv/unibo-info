class Coda: 
    # la tua init 
    def __init__(self):
        self.__items = []
    
    def elementi(self):
        return self.__items
    
    def is_vuota(self):
        return self.__items == []
    
    def accoda(self,el):
        self.__items.insert(0,el)
        return self
    
    def esci(self):
        if len(self.__items)!=0:
            return self.__items.pop()
        return None
            
    def __len__(self):
        return len(self.__items)    

    def __str__(self): 
        return "> "+" ".join(str(e) for e in self.__items)+ " ||"

class CodaPrioritaria(Coda):
        
    def accoda(self,tupla):
        if type(tupla)==tuple and len(tupla)==2 and type(tupla[1] != int):
            super().elementi().insert(tupla[1]-1,tupla)
            return self
        else:
            raise TypeError
       

print(CodaPrioritaria().accoda(("a",1),).esci())
    
