#RECURSION:

#Factorial:
def f(x):
    if x == 1:
        return 1          #It evaluates that f(1)=1
    else:
        return x * f(x-1)

#It knows f(1)=1 so f(2)=2*f(1) therefore it will know the value of f(2) and so on it will know every value automatically

print(f(90))

#DEBUGGING RECURSION:
# WKT: f(n) = n * (n-1) * (n-2) * (n-3) * - - - * 1
# FOR EX: f(4) = 4 * 3 * 2 * 1 i.e; 4 * f(3)
# f(3) = 3 * f(2)
# f(2) = 2 * f(1)
# f(1) = 1 (As defined in line 5 and line 6)
# So  in order to find factorial of 4 the program is executed this way by the computer