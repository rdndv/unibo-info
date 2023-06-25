'''function returns tuple with all proper divisors of n, excluding n'''
def properdivisor(n):
    #code to be fixed
    div = ()
    for i in range(n):
        if n%i = 0:
            div = div + i
    print(div)
    

def properdivisor_fixed(n):
    div = ()
    for i in range(1,n):
        if n%i == 0:
            div = div + (i,)
    return div
