#FUNCTIONS:

#FUNCTIONS ARE USED FOR THEIR REUSABILITY

def myfunction():    #Defining the function
    print('Called')

myfunction()         #Calling function
myfunction()         #Can call multiple times

def fn(x):           #Defining parameter
    print('YO' + ' ' + x)

fn("wassup")         
fn("How you doin'?") #Calling with parameter

def a(x = '0'):      #Defining with default value of parameter
    print('GG' + ' ' + x)

a()
a('1')               #Will overwrite the default value

def ourfn(x):
    return 10*x      #Will return the value in result

print(ourfn(2))

def yourfn(x):
    if x == 0:
        print('ERROR')
        return 0
    else:
        return x
    
yourfn(3)
yourfn(0)
