#TUPLE OPERATIONS:
T = ('apple', 'mango')
if 'mango' in T: #Checks whether the element is available in tuple
    print('yes')
print(len(T)) #Prints number of elements
print(T.index('apple')) #Prints index of the element
del T #Deletes the whole tuple
print(T)