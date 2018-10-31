# module 就是一个python文件(.py结尾的文件)，当被import的时候被加载，而且只能加载一次。
# 重复import不会再次加载。
# python 提供了一些标注库，可以参考：https://docs.python.org/3/library/


print("this is from module1")

def fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a+b