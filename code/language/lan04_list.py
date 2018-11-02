print("***************list支持很多函数************")
# list支持很多函数，例如：
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))

print(fruits.count('tangerine'))

print(fruits.index('banana'))

print(fruits.index('banana', 4))  # Find next banana starting a position 4

fruits.reverse()
print(fruits)

fruits.append('grape')
print(fruits)

fruits.sort()
print(fruits)

fruits.pop()

print("***************把List作为堆栈来使用************")

# 可以把List作为堆栈来使用。
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)

print(stack.pop())

print(stack)

print(stack.pop())

print(stack.pop())

print(stack)


# List Comprehensions
# 这个短语很难翻译成中文，翻译成“列表综合”也不是很恰当，它的作用就是以各种方式生成各种list.
# list comprehension 体现了python语法的强大。

#通常我们生成list都是用下面的方式
squares = []
for x in range(10):
    squares.append(x**2)

print(squares)

# 但是我们可以用更简单的方式来生成。
squares = list(map(lambda x: x**2, range(10)))

# 或者写成这样
squares = [x**2 for x in range(10)]
print(squares)

'''
A list comprehension consists of brackets containing an expression followed by a for clause,
then zero or more for or if clauses.
The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it.
'''
# 下面这里例子是形成一个元组列表的例子
a = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(a)

# 上面的代码如果用一般的方式实现大概是这样
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))
print(combs)

# 下面是list comprehension的一些例子
vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
print([x*2 for x in vec])

# filter the list to exclude negative numbers
print([x for x in vec if x >= 0])

# apply a function to all the elements
print([abs(x) for x in vec])

# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])

# create a list of 2-tuples like (number, square)
print([(x, x**2) for x in range(6)])

# the tuple must be parenthesized, otherwise an error is raised
# print([x, x**2 for x in range(6)])

# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])

# 或者把返回值作为函数的参数直接使用
from math import pi
[str(round(pi, i)) for i in range(1, 6)]

# 下面这个例子是求矩阵的转置。
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print([[row[i] for row in matrix] for i in range(4)])

# 和list comprehension 类似，也有set comprehension
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

# del statement 用来删除list中的元素，它同样可以删除list。
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)

del a[2:4]
print(a)

del a[:]
print(a)

del a
