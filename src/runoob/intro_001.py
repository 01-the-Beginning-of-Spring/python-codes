# -*- coding: utf-8 -*-
#
# @Time 2019-11-07 01:17
#

from utils.console_beautify import *  #导入外部工具包

# 初学者对以下装饰器可以不用理会，去掉后函数也是一样的执行结果

#1 python保留字
@log_simple # 不带参数的装饰器
def print_keywords():
    import keyword
    # 打印所有关键字
    print(keyword.kwlist)
    # 判断一个字符串是否是关键字
    print(keyword.iskeyword('or'))
    print(keyword.iskeyword('Or'))
    print(keyword.iskeyword('main'))

#2 多行语句
@log_advanced() # 带参数的装饰器，使用默认参数
def multi_line():
    var = 1 + \
        2 + \
        4
    print(var)

#3 基本类型
@log_advanced()
def type_basic():
    print(type(1))
    print(type(1.0))
    print(type(True))
    print(type(1+2j))

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

#5 用户输入输出（注意这里：需要在控制台输入文字，然后程序才能继续，否则程序会一直暂停在那里）
@log_advanced()
def user_input():
    user_str = input("请在这里输入：")
    print("你输入的是：", user_str, end="") #不换行输出
    print() #输出空行

#6 一行多条语句
@log_advanced()
def multi_statement():
    import sys; x = 'python-string'; sys.stdout.write(x + '\n')


if __name__ == '__main__':
    #1
    print_keywords()
    #2
    multi_line()
    #3
    type_basic()
    #4
    type_str()
    #5
    user_input()
    #6
    multi_statement()

