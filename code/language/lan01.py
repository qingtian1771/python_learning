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

############### Lists
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


############### 关于字符串的操作符
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

# 可以支持多行字符串
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
# 也可以支持长的字符串分成多行输入
text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)


############### 元组tuple
# 元组就是把一些元素按照顺序去打包，形成一个数据类型。
t = 12345, 54321, 'hello!'
print(t[0])

print(t)

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)

# 元组中的元素是不可更改的。
# t[0] = 88888


# 元组虽然不可更改，但是它可以包含可变对象，例如list对象。
v = ([1, 2, 3], [3, 2, 1])
print(v)

# 可以按照顺序来解包
t = 12345, 54321, 'hello!'
x, y, z = t
print(x,y,z)


############### 集合 Set
# Set是一个集合，其中的元素没有顺序，但不可以重复。
# Set可以支持集合运算，例如并、交、差、异或等。
# Set有两种创建方式，{}或者set()。

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed

print('orange' in basket)                 # fast membership testings

print('crabgrass' in basket)


# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
print(a)                                  # unique letters in a

print(a - b)                              # letters in a but not in b

print(a | b)                              # letters in a or b or both

print(a & b)                              # letters in both a and b

print(a ^ b)                              # letters in a or b but not both

# 和list comprehension 类似，也有set comprehension
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

############### 字典
# 字典类似List，但是有键和值，每个值都可以通过对应的键来存取，键可以是任意类型的对象（字符串、数字、List）
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

# 字典可以用下面的方式初始化
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)

# 可以用下面的方式来访问字典中的所有元素，字典中的元素是没有顺序的。
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

# 删除一个元素,可以用下面的两种方式。
del phonebook["John"]
print(phonebook)
phonebook.pop("Jack")
print(phonebook)

# 另一个字典的例子。
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)

print(tel['jack'])

del tel['sape']
tel['irv'] = 4127
print(tel)

list(tel)
sorted(tel)

print('guido' in tel)
print('jack' not in tel)

# 可以使用dict()这样的构造函数来构造字典。
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

# 和list comprehension类似，也有dict comprehension
a = {x: x**2 for x in (2, 4, 6, 8)}
print(a)

# 当key是字符串时，也可以这么构造一个字典。
print(dict(sape=4139, guido=4127, jack=4098))

############### 循环的一些特殊方式

# 对于字典来讲，可以把key和value一次取出。
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# 可以用enumerate取出index
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# 还可以用zip函数将两个list并列起来。
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# 反转顺序。
for i in reversed(range(1, 10, 2)):
    print(i)

# 排序
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

# 可以对sequence比较大小，以下都是True
print((1, 2, 3) < (1, 2, 4))
print([1, 2, 3] < [1, 2, 4])
print('ABC' < 'C' < 'Pascal' < 'Python')
print((1, 2, 3, 4) < (1, 2, 4))
print((1, 2) < (1, 2, -1))
print((1, 2, 3)  == (1.0, 2.0, 3.0))
print((1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4))