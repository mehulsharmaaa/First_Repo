#Reading files:
F = open('Myfile.txt', 'r')
print(F.read()) #will open the text file in terminal
print(F.read(4)) #specifying the number f characters to be read
print(F.readline()) #read first line

for line in F: #Can be used to reda lines
    print(line)