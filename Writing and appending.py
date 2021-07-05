#Writing and appending:
F = open('Myfile.txt', 'wt') #w stands for write and t for text file
F.write('Hello, This is not me\n') #Clears the previous text and writes the new

F = open('Myfile.txt', 'at') #a stands for append
F.write('Hello, This is me again\n') #will append this text without deleting previous
