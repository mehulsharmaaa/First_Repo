#BREAK AND CONTINUE:

#BREAK:

C = ['apple', 'google', 'microsoft', 'netflix']

i = 0
while i < len(C):
    if C[i] == 'netflix':
        break               #If we don't want the loop to work at a certain point we break
    print(C[i])             #Used to break the loop at desired point
    i += 1

for name in C:
    if name == 'microsoft':
        break
    print(name)

#CONTINUE:

D = ['A', 'B', 'C', 'D']

for a in D:
    if a == 'B':
        continue           #Used to continue the loop without executing the next ommand if the condition is true
    print(a)






    
    