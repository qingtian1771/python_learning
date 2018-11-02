'''
The str() function is meant to return representations of values which are fairly human-readable,
while repr() is meant to generate representations which can be read by the interpreter
(or will force a SyntaxError if there is no equivalent syntax)
'''

s = 'Hello, world.'
print(str(s))

print(repr(s))

print(str(1/7))

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)


# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)

# The argument to repr() may be any Python object:
print(repr((x, y, ('spam', 'eggs'))))

# Here are two ways to write a table of squares and cubes:
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))


# 还可以用0填充
print('12'.zfill(5))

print('-3.14'.zfill(7))

print('3.14159265359'.zfill(5))

# str.format()的使用方式
print('We are the {} who say "{}!"'.format('knights', 'Ni'))

print('{0} and {1}'.format('spam', 'eggs'))

print('{1} and {0}'.format('spam', 'eggs'))

print('This {food} is {adjective}.'.format(
      food='spam', adjective='absolutely horrible'))

print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))

contents = 'eels'
print('My hovercraft is full of {}.'.format(contents))
# !r表示repo()
print('My hovercraft is full of {!r}.'.format(contents))

import math
# 保留三位小数
print('The value of PI is approximately {0:.3f}.'.format(math.pi))

# 格式化输出
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name, phone))


