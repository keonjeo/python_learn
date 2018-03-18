#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 文件名：test.py

if True:
  print "Answer: ",
  print "True"
else:
  print "Answer: ",
  # 没有严格缩进，在执行时会报错
  print "False"


raw_input("按下 enter 键退出，其他任意键显示...\n")


import sys; x = 'runoob'; sys.stdout.write(x + '\n')

counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = "John" # 字符串
 
print counter
print miles
print name