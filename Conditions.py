#CONDITIONS:

#IF:
x = 18
y = -5
if x > -5: #Checks if the condition is true
    print('THE RESULT IS TRUE') #This result will only be printed when the statement is true because of indentation
print('END')

#ELSEIF:
if x<y:
    print(str(x) + 'is less than' + str(y))
elif x>y:
    print(str(x) + ' ' + 'is greater than' + ' ' + str(y)) #Checks elif statement after if statement doesn't satisfy condition

#ELSE:
if x<y:
    print(str(x) + 'is less than' + str(y))
elif x>y:
    print(str(x) + ' ' + 'is greater than' + ' ' + str(y))
elif x==y:
    print(str(x) + ' ' + 'is equal to' + ' ' + str(y))
else:
    print('NOTHING IS PERMANENT') #The code under else will only be executed when all the conditions under if and elif are false

