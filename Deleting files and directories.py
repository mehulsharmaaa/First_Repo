#Deleting files and directories
import os #we need to import os(operating system) functionality in order to remove file from explorer
os.remove('Myfile.txt')

import os 
if os.path.exists('Myfile.txt'): #Checks the existence of file before execution
    os.remove('Myfile.txt')
else:
    print('WRONG FILE NAME')

#os.removedirs('NAME OF DIRECTORY') #Removes the directory
