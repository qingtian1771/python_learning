

import module1

module1.fibonacci(10)
print(dir(module1))

from module1 import fibonacci

fibonacci(10)

import string
print(dir(string))

import foo.bar
# from foo import bar