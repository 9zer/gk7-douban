#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
author by jacksyen[hyqiu.syen@gmail.com]
---------------------------------------
全局配置
"""
import os


DB_CONFIG = {
    'host': '192.168.1.104',
    'user': 'root',
    'passwd': 'root',
    'db': 'gk7_douban',
    'port': 3306
}

# 书籍封面前缀
BOOK_COVER_URL = 'http://img3.douban.com/view/ark_{#type}_cover/retina/public/{#id}.jpg'

# 源文件存储目录
DATA_DIRS = '%s/data' %(os.path.abspath('.'))

BOOK_COVER_DIRS = '%s/cover' %(DATA_DIRS)

# 输出文件存储目录
OUT_DATA_DIRS = '%s/out-data' %(os.path.abspath('.'))

# 输出文件格式
OUT_FILE_FORMAT = 'mobi'

# 书籍图片路径分割字符
BOOK_IMG_PATH_SPLIT = ';'

# 书籍页面分隔符
BOOK_PAGE_SPLIT = 'pagebreak'

# email配置
EMAIL = {
    ## SMTP
    'smtp': 'smtp.gmail.com',
    ## 端口
    'port': 25,
    ## 发送方邮箱
    'user': 'hyqiu.syen@gmail.com',
    ## 发送方密码
    'pwd': '',
    ## 邮件编码
    'encode': 'UTF-8',
    ## 超时时间30秒
    'timeout': 30
}

'''
全局状态
+ 邮件表
+ htmls转换表
'''
STATUS = {
    'wait': 'wait',
    'complete': 'complete',
    'error': 'error'
}

## 日志存储目录
LOG_DIRS = '%s/logs' %(os.path.abspath('.'))
