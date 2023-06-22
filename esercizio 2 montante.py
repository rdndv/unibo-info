'''funzione che restituisce il capitale finale M'''
def capital(C,r,n,t):
    return C*(1+(r/n))**(n*t)


print(capital(1000, 0.08, 12, 2))