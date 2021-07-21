#METHODS AND SELF:
class point:
    x = 0
    y = 0
    def movepoint(self, newX , newY): #Defining method and self is in arguement as the objects we want to change is in self
            self.x = newX             #Setting X coordinate of the object to the newX
            self.y = newY             #Setting Y coordinate of the object to the newY
    def printpoint(self):
        print(str(self.x), str(self.y))

origin = point()
mypoint = point()         
mypoint.movepoint(5,10)               #Calling a method
mypoint.printpoint()