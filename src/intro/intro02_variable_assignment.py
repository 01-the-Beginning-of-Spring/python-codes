# -*- coding: utf-8 -*-
#
# @Time 2019-12-17 22:12
#
from utils.console_beautify import *

# 1 python 变量与赋值
# Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
# 在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。
# 等号（=）用来给变量赋值。
# 等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值

# 2 一个变量可以通过赋值指向不同类型的对象
v = 123
v = True


# 3 函数也可以赋值给变量
def func():
    pass


vfunc = func

# 4 python中特殊的赋值方法
# 4.1 同时给多个变量赋同一个值
v1 = v2 = v3 = 123

# 4.2 同时为多个变量赋不同的值
v1, v2, v3 = 1, 2, 3

# 4.2.1 两个变量交换值
new_segment('两个变量交换值')
v1, v2 = 1, 2
print(v1, v2)
v1, v2 = v2, v1  # 两个变量交换值
print(v1, v2)

# 4.2.2 多个变量交换值
new_segment('多个变量交换值')
v1, v2, v3 = 1, 2, 3
print(v1, v2, v3)
v1, v2, v3 = v3, v1, v2  # 多个变量交换值
print(v1, v2, v3)

# 5 测试变量类型（函数或某种类型）
new_segment('测试变量类型')


# 内置的 type() 函数可以用来查询变量所指的对象类型。
# isinstance()会认为子类是一种父类类型。type()不会认为子类是一种父类类型。
def show_type(var):
    import types
    if isinstance(var, types.FunctionType):  # 判断变量类型是函数
        print('show function ->', var.__name__)
    else:  # 判断变量属于某种类型
        print('show type ->', type(var).__name__, ':', var)


show_type(func)
show_type(None)
show_type('abc')
show_type(123)
show_type(True)

# 6 检查变量类型（函数或某种类型）
new_segment("检查变量类型")


def check_type(var, vtype=None):
    import types
    # chk_result = ''  #这里不用像C语言或其他语言一样初始化
    if isinstance(var, types.FunctionType):
        chk_result = "check function -> {0}".format(var.__name__)
    elif var == None:
        chk_result = "check variable is None"
    elif vtype == None:
        chk_result = "check variable '{0}' is not instanceof '{1}'".format(var, type(vtype).__name__)
    elif type(var) is vtype:
        chk_result = "check variable '{0}' is instanceof '{1}'".format(var, vtype.__name__)
    else:
        chk_result = "check variable '{0}' is not instanceof '{1}'".format(var, vtype.__name__)
    print(chk_result)


'''
new_segment('check type: 1 param')
check_type(check_type)
check_type(None)
check_type('abc')

new_segment('check type: 2 params')
check_type(check_type, None)
check_type(None, None)
check_type('abc', None)
check_type('abc', str)
check_type('abc', int)
'''
