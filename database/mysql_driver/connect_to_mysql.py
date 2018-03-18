#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Python 标准数据库接口为 Python DB-API, Python DB-API为开发人员提供了数据库应用编程接口。
# Python 数据库接口支持非常多的数据库:
#                                 GadFly mSQL MySQL PostgreSQL
#                                 Microsoft SQL Server 2000 
#                                 Informix Interbase Oracle Sybase


# MySQLdb 是用于Python链接Mysql数据库的接口,
# 它实现了 Python 数据库 API 规范 V2.0，基于 MySQL C API 上建立的。

# How to install MySQLdb for python
# sudo python get-pip.py
# sudo pip install MySQL-python

# import the libs you want to use
import MySQLdb

print "========================="
print "     Hello, Python!      "
print "========================="


# 打开数据库连接
db = MySQLdb.connect("localhost","root","","TESTDB" )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()

print "Database version : %s " % data

# 关闭数据库连接
db.close()
