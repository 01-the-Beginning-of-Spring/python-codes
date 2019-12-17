# -*- coding: utf-8 -*-
#
# @Time 2019-12-16 21:47
#

from utils.console_beautify import *  #导入外部工具包

# 1. 编码
# 默认情况下，Python 3 源码文件以 UTF-8 编码，所有字符串都是 unicode 字符串。
# 当然也可以为源码文件指定不同的编码，一般在文件的首行以单行注释的形式设置
# 例如，一般以这样的形式设置，# -*- coding: gb2312 -*-
# 当然不是非得这个形式设置，也可以这样设置， # coding: gb2312

# 2. 注释
# 单行注释，代码中以#开始的行，或代码中#后的部分
# 多行注释，以三个单引号'或三个双引号"引用起来的行

# 3. 行与缩进
# python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} 。
# 缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。否则会导致如下运行错误：
# IndentationError: unindent does not match any outer indentation level

# 4. 空行
# 函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。
# 空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。
# 记住：空行也是程序代码的一部分。

# 5. 标识符
# 第一个字符必须是字母表中字母或下划线 _
# 标识符的其他的部分由字母、数字和下划线组成。
# 标识符对大小写敏感。
# 在 Python 3 中，可以用中文作为变量名，非 ASCII 标识符也是允许的了。

# 6. 保留字
@log_simple # 不带参数的装饰器 初学者可以对装饰器不用理会，去掉后函数也是一样的执行结果
def print_keywords():
    import keyword
    # 打印所有关键字
    print(keyword.kwlist)
    # 判断一个字符串是否是关键字
    print(keyword.iskeyword('or'))
    print(keyword.iskeyword('Or'))
    print(keyword.iskeyword('main'))

# 7. 一条语句在多行中
# Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\)来实现多行语句
# 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)
@log_advanced() # 带参数的装饰器，使用默认参数
def multi_line():
    avar = 1 + 2 + 3\
          + 4 + 5 + 6 + 7 + 8
    print(avar)
    alist = [1, 2, 3,
             4, 5, 6, 7, 8]
    print(alist)

# 8. 一行有多条语句
@log_advanced()
def multi_statement():
    import sys; x = 'python-string'; sys.stdout.write(x + '\n')

# 9. 多个语句构成代码组
# 缩进相同的一组语句构成一个代码块，我们称之代码组。
# 像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
# 我们将首行及后面的代码组称为一个子句(clause)。

# 10. import 与 from...import
# 在 python 用 import 或者 from...import 来导入相应的模块。
# 将整个模块(somemodule)导入，格式为： import somemodule
# 从某个模块中导入某个函数,格式为： from somemodule import somefunction
# 从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
# 将某个模块中的全部函数导入，格式为： from somemodule import *

if __name__ == '__main__':
    print_keywords()
    multi_line()
    multi_statement()
