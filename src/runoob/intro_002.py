# -*- coding: utf-8 -*-
#
# @Time 2019-11-11 14:07
#

# Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
# 在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。

from utils.console_beautify import *


# 初学者对以下装饰器可以不用理会，去掉后函数也是一样的执行结果

# 1~6 判断数据类型
@log_simple  # 不带参数的装饰器
def show_var_type(var):
    print("var type:", type(var).__name__)
    print("var value:", var)


# 7~8 判断是否是函数，并输出函数名称
@log_advanced()  # 带参数的装饰器，使用默认参数
def show_func_name(func):
    import types
    if isinstance(func, types.FunctionType):
        print('function name:', func.__name__)
    else:
        print('输入参数不是函数：[', func, ']')


if __name__ == '__main__':
    # 不同类型的变量
    var_int = 100
    var_float = 100.0
    var_bool = True
    var_complex = 100 + 10j
    var_str = "a-string"
    show_var_type(var_int)  # 1
    show_var_type(var_float)  # 2
    show_var_type(var_bool)  # 3
    show_var_type(var_complex)  # 4
    show_var_type(var_str)  # 5

    # 函数也可以给变量赋值
    var_func = show_var_type
    show_var_type(var_func)  # 6

    # 输出函数名称
    show_func_name(show_var_type)  # 7
    show_func_name(var_int)  # 8
