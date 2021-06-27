#COMPARISON/RELATIONAL OPERATORS:
x,y = 10,20;
r = x == y  #Checks whether LHS = RHS
print(r)

s = x != y #Checks whether LHS is not equals to RHS
print(s)

t = x >= y #Checks whether x is either greater than or equal to y
print(t)

#LOGICAL OPERATORS:

#AND:
q = 25
r = 30
s = (r > q) and (r == q) #AND states that both of the conditions must be satisfied fo result to be true
print(s)

#OR:
t = (r > q) or (r == q) #OR states that if either of the statements are true the reult will be true
print(t)

#NOT:
u = not (r == q) #NOT states that the result will be true if the condition isn't satisfied
print(u)