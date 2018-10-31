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


