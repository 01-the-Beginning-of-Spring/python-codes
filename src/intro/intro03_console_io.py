# -*- coding: utf-8 -*-
#
# @Time 2019-12-17 12:27
#

from utils.console_beautify import *

# 1. 用户控制台输入输出
# 用户控制台输入： input() 函数
# 控制台输出信息： print() 函数
# 注意：这里需要在控制台输入文字，然后程序才能继续，否则程序会一直暂停在那里
@log_advanced()
def user_input_output():
    user_str = input("请在这里输入：")
    print("你输入的是：[" + user_str + ']', end="") #不换行输出
    print() #输出空行

if __name__ == '__main__':
    user_input_output()
