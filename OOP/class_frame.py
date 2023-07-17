# non inserire print o test

class PilaVuotaException(Exception):
    pass

class Pila:
    def __str__(self): # NON MODIFICARE!
        return "^\n"+"".join(str(e)+"\n" for e in self.__elementi[::-1])+ "_"
    
    # definire QUI i metodi di Pila
    def __init__(self):
        self.__elementi = []
    
    def __len__(self):
        return len(self.__elementi)
    
    def is_empty(self):
        return len(self.__elementi) == 0
    
    def push(self,other):
        self.__elementi.append(other)
        return self
        
    def pop(self):
        if len(self.__elementi)==0:
            raise PilaVuotaException("Pila Vuota")
        return self.__elementi.pop()
    
    def get(self):
        return self.__elementi

class PilaPazza(Pila):
    def pop(self):
        r = super().get()
        if len(r)==0:
            raise PilaVuotaException("Pila Vuota")
        ultimo = r.pop()
        r.append(ultimo)
        return ultimo
    
P = PilaPazza()
print(P)
P.push('Andrea').push('Beatrice').push('Carl').push('Dani')
print(P)
print(P.pop())
print(P.pop())
print(P)


    
    
