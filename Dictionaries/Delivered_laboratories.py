D = {}


def add_student_lab(student, n_lab):
    '''function to add students and all laboratories delivered and return dictionary'''
    if student not in D:
        D[student] = n_lab
    else:
        D[student]+= n_lab
        
    return D
print(add_student_lab(('Renata'),[1,2,3,5])),
print(add_student_lab(('Dániel'),[1,4,5,9,11]))
print(add_student_lab(('Renata'),[4]))


def lab_num(name):
    '''return a list containing all laboratories a specific student has delivered, if student not in the dictionary, return empty list'''
    for student in D:
        if name == student:
            return D.get(student,[])
    return []
        
print(lab_num('Renata'))
print(lab_num('Dániel'))
print(lab_num('Kika'))


def who_delivered(n):
    '''return a list with all student that has delivered laboratory n, if none, returns empty list'''
    L = []
    for keys in D:
        if n in D[keys]:
            L.append(keys)
    return L

print(who_delivered(0))

def frequency():
    '''return a new dictionary containing the frequency of all delivered laboratories'''
    frequency = {}
    lab = (list(D.values()))
    for values in lab:
        for laboratory in values:
            if laboratory not in frequency:
                frequency[laboratory] = 1
            else:
                frequency[laboratory] += 1
    return frequency
            
print(frequency())
