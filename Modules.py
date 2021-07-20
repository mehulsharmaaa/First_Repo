#MODULES:(MODULES ARE BASICALLY LIBRARIES IN PYTHON)

import Functions #Imports Functions file from the repository which means we can use the functions that were defined there

print(Functions.fn('0')) #Calling the function with parameter in this module

import Recursion as f  #importing a file as desired name
print(f.f(15))

import platform #Those libraries/modules can be also imported which aren't created by us
print(platform.version()) #Version tells us about the version of the platform we're currently using

print(f.j) #Variables can be imported too

from Recursion import f #Importing a particular function from a file
print(f(3))