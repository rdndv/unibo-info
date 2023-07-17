class Seq:
    def __init__(self,seque):
        self.__s=seque
    #INSERIRE QUI ALTRI METODI SOLO SE
        
    def get(self):
        return self.__s

def prefs(S):
    #INSERIRE LA SOLUZIONE QUI
    #NON INSERIRE PRINT: solo i return delle funzione
    S = list(S.get()) #trasformo qualsiasi sequenza in lista per cosi 

    if len(S)==0:
        return 0
    #if type(S) != str:
     #   S = 
    #caso limiti dove la stringa è vuota, quindi avrà 0 prefissi distinti
    ns = [S[-1]]
    for i in range(len(S)-1):
        if S[i]!=S[i+1]:
            ns.append(S[i])
            
    return len(ns)         
        
        
print(prefs(Seq({1:"renata", 2:"alo", 1:"quem"})))
