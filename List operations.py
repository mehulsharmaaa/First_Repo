#LIST OPERATIONS:
L = ['apple', 'google']
if 'apple' in L: #To check availability of a element
    print('yes')
print(len(L)) #Number of elements inside list
L.append('Microsoft') #adds element to the list
L.insert(0, 'Sony') #adds element at desired index
L.remove('Sony') #removes element
L.pop(1) #removes element on the basis of index number
L.replace(0) = 'cherries' #replaces element
del L[0] #deletes element at desired index
L.clear() #clears all the elements form the list
print(L)

M = [1,3,2]
M.sort() #arranges the elements
print(L + M) #combines two lists
print(max(M)) #gives maximum value
print(min(M)) #gives minimum value
