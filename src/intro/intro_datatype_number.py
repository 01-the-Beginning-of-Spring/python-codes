# -*- coding: utf-8 -*-
#
# @Time 2019-12-16 22:48
#

from utils.console_beautify import *  #导入外部工具包

# 数字(Number)类型
# python中数字有四种类型：整数、布尔型、浮点数和复数。
# int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
# bool (布尔), 如 True。
# float (浮点数), 如 1.23、3E-2
# complex (复数), 如 1 + 2j、 1.1 + 2.2j

# 1. Number 类型
@log_advanced()
def type_basic():
    print(type(1))
    print(type(1.0))
    print(type(True))
    print(type(1+2j))

new_segment("Number(数字）: int, float, bool, complex")
var_int = 100  # 长整型，没有 python2 中的 long
var_float = 100.0
var_bool = True
var_complex1 = 100 + 10j
var_complex2 = complex(123, 321)
# 在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。
# 到 Python3 中，把 True 和 False 定义成关键字了，但它们的值还是 1 和 0，它们可以和数字相加。
print(type(True) == bool)
var_int_original = 1000
var_int_add_true = var_int_original + True
var_int_add_false = var_int_original + False


if __name__ == '__main__':
    type_basic()
