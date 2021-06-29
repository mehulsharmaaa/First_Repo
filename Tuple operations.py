#TUPLE OPERATIONS:
T = ('apple', 'mango')
if 'mango' in T: #Checks whether the element is available in tuple
    print('yes')
print(len(T)) #Print number of elements
print(T.index('apple')) #Prints index of the element
#del T #Deletes the whole tuple
print(T)

#UNPACKING TUPLES:
ABC = ('I', 'AM', 'FREAK')
a, b, c = ABC
print(a)
print(b)
print(c)

#NESTING TUPLES: Combining two tuples but each tuple retain its identity
print(T + ABC)


