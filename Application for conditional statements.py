#CHECKING WHETHER A NUMBER IS POSITIVE NEGATIVE OR ZERO:
x = float(input('ENTER A NUMBER: '))
if x>0:
    print(str(x) + ' ' + 'is positive')
elif x<0:
    print(str(x) + ' ' + 'is negative')
else:
    print('THE NUMBER IS ZERO')