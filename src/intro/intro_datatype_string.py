# -*- coding: utf-8 -*-
#
# @Time 2019-12-16 22:50
#

from utils.console_beautify import *  #导入外部工具包

# 字符串(String)
# python中单引号和双引号使用完全相同。
# 使用三引号('''或""")可以指定一个多行字符串。
# 转义符 '\'
# 反斜杠可以用来转义，使用r(指raw)可以让反斜杠不发生转义。 如 r"this is a line with \n" 则\n会显示，并不是换行。
# 按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
# 字符串可以用 + 运算符连接在一起，用 * 运算符重复。
# Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
# Python中的字符串不能改变。
# Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
# 字符串的截取的语法格式如下：变量[头下标:尾下标:步长]

#4 字符串
@log_advanced()
def type_str():
    str = 'Runoob'
    print(str)  # 输出字符串，以下四行俗称"切片"
    print(str[0:-1]) # 输出第一个到倒数第二个的所有字符
    print(str[2:5])  # 输出从第三个开始到第五个的字符
    print(str[2:])   # 输出从第三个开始后的所有字符
    print(str[::-1]) # * 倒序输出
    print(str[0])    # 输出字符串第一个字符
    print(str * 2)   # 输出字符串两次
    print(str + '你好')      # 连接字符串
    print('hello\nrunoob')   # 使用反斜杠(\)+n转义特殊字符
    print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
    str = '''
    1-多行字符串 第一行
    2-多行字符串 第二行
    '''
    print(str)

# 通过打印字符串详情，查看字符串具体内容
@log_simple
def check_str(cmt, vstr):
    print(cmt, "=", "[", end='')
    print(vstr, end='')
    print("]")

if __name__ == '__main__':
    type_str()
    print("this ""is ""string")

    new_segment("字符串")
    # Python中的字符串不能改变。
    # Python中的字符串用单引号 ' 或双引号 " 括起来，同时使用反斜杠 \ 转义特殊字符
    s1 = 'abcdefg' + 'ABCDEFG'  # 加号 + 是字符串的连接符
    s2 = "ABCDEFG " * 2  # 星号 * 表示复制当前字符串，紧跟的数字为复制的次数
    s3 = 'ABCD\tABCD'
    s4 = r'ABCD\tABCD'  # 反斜杠可以用来转义，使用r可以让反斜杠不发生转义
    s5 = r"ABCD\tABCD"
    s6 = '''ABCD\tABCD
    一个可换行的字符串'''
    s7 = """ABCD\tABCD
    另一个可换行的字符串"""
    s8 = r'''ABCD\tABCD
    ABCD'''
    s9 = r"""ABCD\tABCD
    ABCD""" + 'XYZ'
    check_str('s1', s1)  # 1
    check_str('s2', s2)  # 2
    check_str('s3', s3)  # 3
    check_str('s4', s4)  # 4
    check_str('s5', s5)  # 5
    check_str('s6', s6)  # 6
    check_str('s7', s7)  # 7
    check_str('s8', s8)  # 8
    check_str('s9', s9)  # 9

    ##4
    new_segment("字符串切片")
    # 字符串切片的格式是：变量[头下标:尾下标:步长]，其中步长可省略
    # Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始
    s = 'ABCDEF'
    print(s, s[:])
    print(s[-2], s[-1], s[0], s[1], s[2], sep=',')
    print(s[-2:], s[-1:], s[0:], s[1:], s[2:], sep=',')
    print(s[:-2], s[:-1], s[:0], s[:1], s[:2], sep=',')
    print(s[::1], s[::2], s[::3], sep=',')
    print(s[1:4:1], s[1:4:2], sep=',')