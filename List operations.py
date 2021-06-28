#LIST OPERATIONS:
L = ['apple', 'google']
if 'apple' in L: #To check availability of a element
    print('yes')
print(len(L)) #Number of elements inside list
L.append('Microsoft') #adds element to the list
L.insert(0, 'Sony') #adds element at desired index
L.remove('Sony') #removes element
del L[0] #deletes element at desired index
L.clear()
print(L)