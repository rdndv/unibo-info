def fibonacci(n):
    '''returns a list with a sequence of all Fibonaci numbers from fibonacci(0) to fibonacci(n)'''
    if n<0:
        return []
    if n==0:
        return [0]
    if n==1:
        return [0,1]
    lista = fibonacci(n-1)
    lista.append(lista[-1]+lista[-2])
    return lista
