#DICTIONARIES:

D = {'Apple' : 1, 'Mango' : 2, 'Banana' : 3} #Key and key value is defined inside a dictionary
print(D['Apple']) #Accessing a key value through key
print (D.get('Apple')) #Accessing a key value through key
D['Banana'] = 4 #Changing the key value
print(D)
print(D.get('Apple')) #Will get key value for a particualr key

for fruits in D: #Looping in a dictionary
    print(fruits) #Will get the key
    print(D[fruits]) #Will get the key values

for fruits in D.values():
    print(fruits) #Will get the key values too

for fruits, index in D.items():
    print(fruits, index) #Will get key and key values

if 'Apple' in D:
    print('yes') #Checking availability of a key in dictionary
if 1 in D.values():
    print('yes') #Checking availability of a key value in dictionary

D['Cherries'] = 3 #Adding items to the dictionary
print(D)

del D['Banana'] #Deleting items from a dictionary
print(D)

