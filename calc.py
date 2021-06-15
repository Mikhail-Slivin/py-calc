# title here
print("="*100)
title = "Smart Calculator"
print('It is me, ', title)
print("-" * 100)

op = input("Please, enter operation:")
a = int(input('a = '))
b = int(input('b = '))

if op == '+':
    print('a + b =', a + b)
elif op == '-':
    print('a - b =', a - b)
elif op == '*':
    print('a * b =', a * b)
elif op == '/':
    if a or b != 0:
        print("Oops, division by zero")
    else:
        print('a / b =', a / b)
else:
    print('I do not know, what you want(((')
