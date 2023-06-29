def sum_odd(n):
    '''returns sum of all first n odd numbers'''
    if n<=0:
        return 0
    if n == 1:
        return 1
    else:
        return (n*2)-1+ sum_odd(n-1)
