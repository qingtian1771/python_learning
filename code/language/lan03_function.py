# this file shows function

# 这样定义一个函数
def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)

# 函数的第一行是这个函数的documentation string,一般是这个函数的帮助文档。
print(fib.__doc__)

# fib 本身是一个function类型的对象
print(fib)

# 既然是对象就可以赋值，被赋值的对象就可以作为一个函数被调用。
f = fib
f(100)

# function都有返回值，无论有没有return,没有return的情况下的返回值是None
print(fib(100))

# 例如我们还可以写一个函数返回所有的fibonacci数列。
def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result

f100 = fib2(100)    # call it
print(f100)                # write the result

# 可以定义一个函数它的参数含有缺省值
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

# 你可以试试下面的三种调用方式
# ask_ok('Do you really want to quit?')
# ask_ok('OK to overwrite the file?', 2)
# ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

print("----------------参数的初始化方式-------------")
# 参数的缺省值只能初始化一次
i = 5
def f(arg=i):
    print(arg)
i = 6
f()

# 但是如果参数的缺省值是一个可变量，例如list, Dictionary, 或者一个类的实例，那么它就是可变的。
def f(a, L=[]):
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))

# 采用下面的小技巧可以使L不可变。
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))

print("----------------关键字参数-------------")
# 关键字参数。调用函数的时候也可以使用关键字。
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

# 调用的时候可以和位置参数混合搭配来使用。
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

# 下面这些调用是无效的。
# parrot()                     # required argument missing
# parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
# parrot(110, voltage=220)     # duplicate value for the same argument
# parrot(actor='John Cleese')  # unknown keyword argument

print("----------------多参数-------------")
# 函数中使用多个参数的方式
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

# 其中 *arguments 表示函数可以接收多个参数，相当于一个argument的List
# 其中 **keywords 表示可以接收一个字典作为参数。
# 注意下面调用函数的方式
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# 多参数的另外一个例子
def concat(*args, sep="/"):
    return sep.join(args)

print(concat("earth", "mars", "venus"))
print(concat("earth", "mars", "venus", sep="."))

print("----------------多参数的打开方式传入-------------")
# 多参数的打开方式，可以把参数放在一个List中，然后用*的方式去打开。
list(range(3, 6))            # normal call with separate arguments
args = [3, 6]
list(range(*args))            # call with arguments unpacked from a list

# 多参数的打开方式，可以把参数放在一个Dictionary中，然后用**的方式去打开。
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")
d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)

print("----------------在函数中使用lambda表达式-------------")
# lambda表达式只是语法糖
def make_incrementor(n):
    return lambda x: x + n
print(make_incrementor(42))
f = make_incrementor(42)
print(f(0))
print(f(1))







