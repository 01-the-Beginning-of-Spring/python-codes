# -*- coding: utf-8 -*-
#
# @Time 2019-11-25 10:23
#

# 两个变量交换值

if __name__ == '__main__':
    a = 100
    b = 'A-String'
    print(a, b, sep=', ')
    a, b = b, a
    print(a, b, sep=', ')
