def position(car,s):
    '''code to be fixed'''
    if el in s:
        return None
    
    for i in range(s):
        if s[i] == el:
            return s[i]

def position_fixed(car,s):
    '''fixed code'''
    if el not in s:
        return None
    
    for i in range(len(s)):
        if s[i] == el:
            return i
