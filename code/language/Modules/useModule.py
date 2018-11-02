

import module1

module1.fibonacci(10)
print(dir(module1))

from module1 import fibonacci

fibonacci(10)

import string
print(dir(string))

import foo.bar
# from foo import bar

# 导入fibo module
import fibo

# 使用fibo中的函数。
fibo.fib(1000)

print(fibo.fib2(100))

print(fibo.__name__)

import fibo as fib
fib.fib(500)

from fibo import fib as fibonacci
fibonacci(800)

# python在哪里寻找一个module呢？
import sys
print(sys.path)

print(dir(fibo))
print(dir(sys))

# 下面可以列出build in function and variable.
import builtins
print(dir(builtins))
