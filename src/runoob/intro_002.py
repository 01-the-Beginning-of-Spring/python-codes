# -*- coding: utf-8 -*-
#
# @Time 2019-11-11 14:07
#

# Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
# 在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。
# Python3 中有六个标准的数据类型：
# 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
# 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。

# 导入工具包，美化控制台输出
from utils.console_beautify import log_simple, log_advanced, new_segment


# 初学者对以下装饰器[以@开头的行]可以不用理会，去掉后函数也是一样的执行结果

# 私有函数
def __check_and_show_var(var, chk_type):
    print("var type:", type(var).__name__)  # 内置的 type() 函数可以用来查询变量所指的对象类型。
    print("var value:", var)
    import types
    # chk_line = ''  #这里不用像C语言或其他语言一样初始化
    if type(var) == chk_type:  # isinstance()会认为子类是一种父类类型。type()不会认为子类是一种父类类型。
        chk_line = "'{0}' is instance of '{1}'".format(var, chk_type)
    else:
        chk_line = "'{0}' is not instance of '{1}'".format(var, chk_type)
    print(chk_line)


# 判断和展示数据类型
@log_simple  # 不带参数的装饰器
def check_and_show_var(var, chk_type):
    __check_and_show_var(var, chk_type)


# 判断和展示数据类型
@log_simple
def check_and_show_var_list(var_type_list):
    for var, chk_type in var_type_list:
        __check_and_show_var(var, chk_type)


# 判断是否是函数，并输出函数名称
@log_advanced()  # 带参数的装饰器，使用默认参数
def show_func_name(func):
    import types
    if isinstance(func, types.FunctionType):
        print('输入的函数名称是:', func.__name__)
    else:
        print('输入参数不是函数：[', func, ']')


if __name__ == '__main__':
    ## 1
    new_segment('python中特殊的赋值方法')
    # 同时给多个变量赋同一个值
    v1 = v2 = v3 = 123
    check_and_show_var_list([(v1, int), (v2, int), (v3, int)])  # 1
    # 同时为多个变量赋不同的值
    v1, v2, v3 = 1, 2, 3
    check_and_show_var_list([(v1, int), (v2, int), (v3, int)])  # 2
    # 一个变量可以通过赋值指向不同类型的对象
    v1 = True
    check_and_show_var(v1, int)  # 3
    # 函数也可以赋值给变量
    var_func = check_and_show_var
    show_func_name(var_func)  # 4

    ## 2
    new_segment("Number(数字）: int, float, bool, complex")
    var_int = 100  # 长整型，没有 python2 中的 long
    var_float = 100.0
    var_bool = True
    check_and_show_var(var_int, int)  # 1
    check_and_show_var(var_float, float)  # 2
    check_and_show_var(var_bool, bool)  # 3
    var_complex1 = 100 + 10j
    var_complex2 = complex(123, 321)
    check_and_show_var(var_complex1, complex)  # 4
    check_and_show_var(var_complex2, complex)  # 5
    # 在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。
    # 到 Python3 中，把 True 和 False 定义成关键字了，但它们的值还是 1 和 0，它们可以和数字相加。
    check_and_show_var(True, int)  # 6
    print(type(True) == bool)
    var_int_original = 1000
    var_int_add_true = var_int_original + True
    var_int_add_false = var_int_original + False
    check_and_show_var_list([(var_int_original, int), (var_int_add_true, int), (var_int_add_false, int)])  # 7
