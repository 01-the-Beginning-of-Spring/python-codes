# -*- coding: utf-8 -*-
#
# @Time 2019-12-17 22:12
#
from utils.console_beautify import *



# python中特殊的赋值方法
# 同时给多个变量赋同一个值
v1 = v2 = v3 = 123

# 同时为多个变量赋不同的值
v1, v2, v3 = 1, 2, 3

# 两个变量交换值
v1 = 1
v2 = 2
print(v1, v2)
v1, v2 = v2, v1
print(v1, v2)

# 一个变量可以通过赋值指向不同类型的对象
v = 123
v = True

# 函数也可以赋值给变量
def func():
    pass
vfunc = func


new_segment('python中特殊的赋值方法')
# Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
# 在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。
# 等号（=）用来给变量赋值。
# 等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值

# Python3 中有六个标准的数据类型：
# 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
# 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。


# 判断是否是函数，并输出函数名称
def show_func_name(func):
    import types
    if isinstance(func, types.FunctionType):
        print('输入的函数名称是:', func.__name__)
    else:
        print('输入参数不是函数：[', func, ']')


# 判断和展示数据类型
def check_and_show_var(var, chk_type):
    print("var type:", type(var).__name__)  # 内置的 type() 函数可以用来查询变量所指的对象类型。
    print("var value:", var)
    import types
    # chk_line = ''  #这里不用像C语言或其他语言一样初始化
    if type(var) == chk_type:  # isinstance()会认为子类是一种父类类型。type()不会认为子类是一种父类类型。
        chk_line = "'{0}' is instance of '{1}'".format(var, chk_type)
    else:
        chk_line = "'{0}' is not instance of '{1}'".format(var, chk_type)
    print(chk_line)
