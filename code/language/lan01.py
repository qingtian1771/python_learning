# 最简单的输出语句
print("This line will be printed.")

# python使用缩进来控制代码的执行范围
x = 1
if x == 1:
    # indented four spaces
    print("x is 1.")

#Python 完全是面向对象的，是动态类型的，使用前不需要声明或者定义类型，python中的每个变量都是对象。

# 数字
# python支持两种类型的数字，整形和浮点型。
myint = 7
print(myint)
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

# 字符串可以用但引号或者双引号定义，用双引号的好处是它可以包含但引号。
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)
mystring = "Don't worry about apostrophes"
print(mystring)

# 字符串也可以支持+号，它的作用就是将两个字符串连接起来，
one = 1
two = 2
three = one + two
print(three)
hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

# 在一行中可以为多个变量赋值
a, b = 3, 4
print(a,b)

# 但是不能把数字和字符串加起来。
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
one = 1
two = 2
hello = "hello"
# print(one + two + hello)

# Lists类似于数组，可以包含任意变量类型，数量也没有限制。
# Lists可以使用多种方式来访问，下标或者循环。
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

# prints out 1,2,3
for x in mylist:
    print(x)

# 如果访问的下标不存在，那么会产生越界错误。
# IndexError: list index out of range
mylist = [1,2,3]
#print(mylist[10])

# 数字可以进行加减乘除的运算
number = 1 + 2 * 3 / 4.0
print(number)
# 还可以进行取余数的运算
remainder = 11 % 3
print(remainder)
# 或者几次方的运算
squared = 7 ** 2
cubed = 2 ** 3

# 虽然字符串和数字不能使用+号，但是可以使用*号来使一个字符串重复多次。
lotsofhellos = "hello" * 10
print(lotsofhellos)

# 对于数组也可以使用+号，它的作用是把两个数组连接起来。
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

# 数组乘以整数的结果就是重复多次。
print([1,2,3] * 3)

# 格式化字符串。python使用c语言风格的字符串格式化方式。
name = "John"
print("Hello, %s!" % name)

# 使用下面tuple的方式来格式化多个变量。
name = "John"
age = 23
print("%s is %d years old." % (name, age))

# 任何不是字符串的变量也可以使用%s来作为字符串输出。
mylist = [1,2,3]
print("A list: %s" % mylist)

# 常用的输出方式如下：
# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)

# 关于字符串的操作符
astring = "Hello world!"
# 可以取得字符串的长度。
print(len(astring))
# 某个字符首次出现的位置。
print(astring.index("o"))
# 可以计算某个字符出现的次数
print(astring.count("l"))

# 可以取一个字符串的其中一些字符，例如下面取的是索引为3,4,5,6的几个字符。
print(astring[3:7])
# 还可以加步长，用[start:stop:step]的方式。
print(astring[3:7:2])
# 可以使用步长为-1来倒转一个字符串。
print(astring[::-1])
# 可以将一个字符串变成大写和小写。
print(astring.upper())
print(astring.lower())
# 判断字符串是不是以某个字符串开头或者结尾。
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))
# 可以用某个字符分割字符串
afewwords = astring.split(" ")
print(afewwords)



