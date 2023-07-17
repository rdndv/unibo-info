class Nodo:
    def __init__(self, e):
        # QUI completare
        if type(e)!=str:
            raise TypeError
        self.__etichetta = e
        self.__vicini = []

    def aggiungi_vicino(self, n):
        if not isinstance(n, Nodo):
            raise TypeError
        if n not in self.__vicini:
            self.__vicini.append(n)
        return self

    def get_etichetta(self):
        return self.__etichetta

    def __eq__(self,other):
        if type(other)!= Nodo:
            return False
        return self.__etichetta == other.__etichetta
    
    def __str__(self):
        desc = "nodo " + self.__etichetta 
        desc += " con " + str(len(self.__vicini)) + " vicini"
        return desc


class NodoConValore(Nodo):
    def __init__(self, e, v):
        super().__init__(e)
        if type(v)!=int:
            raise TypeError("solo interi")
        self.__valore = v
    
    def __eq__(self,other):
        if type(other)!= NodoConValore:
            return False
        r = super().__eq__(other)
        return r.get() == other.__etichetta

    def __str__(self):
        desc = super().__str__()
        desc += " e valore " + str(self.__valore)
        return desc
