A = 'Get a life'
#Every character of the string has a index
print(A[0])
#Result will be the letter at index 0

#SLICING STRINGS:
#Getting multiple characters as a result:
print(A[0:5])
#Here character at index position 5 is excluded

#LENGTH OF A STRING:
print(len(A))

#GETTING RID OF WHITE SPACES:
X = '  I will not    '
print(X.strip())

#CHANGING A STRING INTO UPPERCASE/LOWERCASE:
Y = 'yes sir'
print(Y.capitalize())
#The first letter will be capitalized in result

print(Y.upper())
#Whole sentence will be capitalized

Z = 'sHUT UP'
print(Z.lower())
#Whole sentence will be in lowercase

#REPLACING CHARACTERS:
x = 'hehe'
print(x.replace('e','a'))

#SPLITTING THE CHARACTERS:
y = 'he he he'
print(y.split(' '))
#It will split wherever there will be a space