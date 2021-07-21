#CLASSES, ATTRIBUTES AND INSTANCES:
class myfirstclass: #Creating a class
    x = 10
    Name = ''  #x and name are attributes of this class
instance1 = myfirstclass()  #This is basically a object of the class
instance2 = myfirstclass()  
instance1.x = 5 #Accesing the value of the object from instance1 and changing its value
print(instance1.x)
print(instance2.x)

