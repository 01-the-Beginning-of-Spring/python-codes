# -*- coding: utf-8 -*-
#
# @Time 2019-12-17 16:54
#

import os

def listFiles(rootPath):
    '''
    广度优先搜索，查找指定目录下所有文件，并返回。
    返回形式：[(filepath, filename), ...]
    '''
    dirList = []
    fileList = []
    dirList.append(rootPath)
    while len(dirList) != 0:
        dirItem = dirList.pop()
        for item in os.listdir(dirItem):
            fullItem = os.path.join(dirItem, item)
            if os.path.isdir(fullItem):
                dirList.append(fullItem)
            else:
                fileList.append((dirItem, item))
    return fileList