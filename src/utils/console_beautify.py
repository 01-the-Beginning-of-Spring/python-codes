# -*- coding: utf-8 -*-
#
# @Time    2019-11-12 12:19
# @author  JacobCN
#

from functools import wraps

# 全局变量
__cnt_simple = 0  # 全局计数器
__sep_clr_font = '\033[95m'  # 分隔行字体颜色，紫红色
__sep_clr_end = '\033[0m'  # 字体颜色设置结束符


# 不带参数的装饰器示例
def log_simple(func):
    """
    装饰器： 美化代码打印。
    格式：#<程序执行总次数> - [<执行函数的名称>]-<该函数执行次数> <输出30个等号（=）>
    """

    __cnt_func = 0

    @wraps(func)  # make original '__name__' is still original name
    def wrapper(*args, **kwargs):
        global __cnt_simple #函数内部修改全局变量
        __cnt_simple += 1
        nonlocal __cnt_func #函数内部修改父级作用域的局部变量
        __cnt_func += 1
        line = __sep_clr_font + '#' + str(__cnt_simple) \
               + ' - [' + func.__name__ + ']-' + str(__cnt_func) \
               + ' ' + ('=' * 30) + __sep_clr_end
        print(line)
        r = func(*args, **kwargs)
        print()
        return r

    return wrapper


# 带参数的装饰器示例
def log_advanced(sep: str = '=', n: int = 30):
    """
    装饰器，美化代码打印。

    格式：#<程序执行总次数> - [<执行函数的名称>]-<该函数执行次数> <n个sep组成的字符串>

    :param sep: 分割符号，默认值 '-'
    :param n: 分割符号数量，默认值 30
    """

    def decorator(func):
        __cnt_func = 0

        @wraps(func)
        def wrapper(*args, **kwargs):
            global __cnt_simple
            __cnt_simple += 1
            nonlocal __cnt_func
            __cnt_func += 1
            line = __sep_clr_font + '#' + str(__cnt_simple) \
                   + ' - [' + func.__name__ + ']-' + str(__cnt_func) \
                   + ' ' + (sep * n) + __sep_clr_end
            print(line)
            r = func(*args, **kwargs)
            print()
            return r

        return wrapper

    return decorator
