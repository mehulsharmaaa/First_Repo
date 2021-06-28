#PYTHON DATA STRUCTURES:

#LISTS: Collection of ordered and changable elements
L = ['Chrome', 'Safari', 'Firefox', 'Opera']
print(L)
print(L[0]) #Prints the element at index position 0
L[1] = 'UC' #Changes the value at index position 1
print(L)

#TUPLES: Collection of ordered and immutable elements
T = ('apple','google','mcrosoft')
print(T)
#The difference between a list and a tuple is that the values can be changed in lists

#SETS: Collection of unordered and unindexed elements and elements can't be repeated
S = {'apple', 'google', 'Microsoft'}
S.add('Sony') #Will add this element 
S.update(['asus', 'toshiba']) #Will add multiple values
S.remove('apple') #Will remove the element
S.discard('alpha') #It will remove the element but if the element specified isn't in the set it won't show any error
print(S)
print(len(S)) #Prints number of elements inside set
 
