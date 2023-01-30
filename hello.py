import time


def hello_world(name):
    print("{name}:你好".format(name=name))

name = "张三"
hello_world(name)


def sum(n):
    res = 0
    for i in range(n+1):
        res = res + i
        print(res)
        time.sleep(1)
    print(res)
# 1+2+3+4+5
n = 100
sum(n)

def sum_2():
    n = 1+1
    print(n)

sum_2()