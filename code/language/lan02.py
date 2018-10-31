############### 条件和判断

# python判断的结果是boolean类型
x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True

# and 和 or操作符
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")
if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

# 可以使用in操作符来判断一个对象是否被包含在一个可列对象中，例如一个list中。
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

# if和else的使用方式。
x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")

# is 用来判断两个对象是不是同一个对象。
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False

# not 操作符的作用就是取反。
print(not False) # Prints out True
print((not False) == (False)) # Prints out False

############### 循环

# 给定一个序列，可以用for做循环。
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

# for循环还可以用在range里面。
for x in range(5):
    print(x) # Prints out the numbers 0,1,2,3,4
for x in range(3, 6):
    print(x) # Prints out 3,4,5
for x in range(3, 8, 2):
    print(x) # Prints out 3,5,7

# while循环的使用方式，Prints out 0,1,2,3,4
count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1

# 一个while的例子，Fibonacci series:
print("Following is an example of while loop to print fibonacci series. ")
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b


# break用于跳出当前循环，continue用于跳过本次循环余下的语句，直接开始一次循环。
# Prints out 0,1,2,3,4
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)

# 可以在while和for循环中使用else，这一点有点不一样。
# Prints out 0,1,2,3,4 and then it prints "count value reached 5"
count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))
# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")

############### 函数

#用def来定义函数
def my_function():
    print("Hello From My Function!")

# 函数可以接受参数
def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

# 函数可以有返回值，使用关键字return
def sum_two_numbers(a, b):
    return a + b

# 可以用下面的方式调用函数
# print(a simple greeting)
my_function()

#prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe", "a great year!")

# after this line x will hold the value 3!
x = sum_two_numbers(1,2)

############### 类和对象

# Objects are an encapsulation of variables and functions into a single entity.
# Objects get their variables and functions from classes. Classes are essentially a template to create your objects.
# # A very basic class would look something like this:
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

# 可以用下面的方式实例化一个类，结果就是一个对象。
myobjectx = MyClass()

# 可以访问这个对象中的变量
myobjectx.variable
print(myobjectx.variable)

# 可以创建多个实例，它们之间是彼此独立的
myobjectx = MyClass()
myobjecty = MyClass()
myobjecty.variable = "yackity"
print(myobjectx.variable)
print(myobjecty.variable)

#也可以调用函数
myobjectx.function()


