#TRY AND EXPCEPT:

try:
    F = open('f.txt', 'x')
    F.write('Hello, I am back!')
except:                           #If the code under try is wrong it won't show error but will execute the code under except
    print('error')


try:
    F = open('f.txt', 'x')
    F.write('Hello, I am back!')  #This file already exist so can't create another
    print(x)                      #x isn't specified
except NameError:                 #You can specify the type of error
    print('Name error')
except FileExistsError:           #Multiple excepts can be used for multiple errors
    print('File exist error')

try:
    F = open('f.txt', 'w')
    F.write('Hello, I am back again!')  
except FileExistsError:               
    print('File exist error')
finally:
    F.close()                    #Closes the file
    print('END')
