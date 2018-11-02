# 类就像任何函数一样必须先定义才能使用。

# 这是定义一个类
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

# 这是实例化这个类
x = MyClass()

# 调用属性和函数
print(x.i)
print(x.f())
print(x.__doc__)

# 一个类可以包含初始化函数__init__，当类构造的时候会自动调用这个函数。
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r, x.i)

# 一个类可以包含两种有效的属性，data attribute 和 method。
# 数据属性不需要定义，它可以随时插入到类的实例
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
