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

#################     前提条件       ##################
#1. 已经创建了数据库 TESTDB.
#2. 在TESTDB数据库中您已经创建了表 EMPLOYEE
#3. EMPLOYEE表字段为 FIRST_NAME, LAST_NAME, AGE, SEX 和 INCOME。
#4. 连接数据库TESTDB使用的用户名为 "testuser" ，密码为 "test123"。
#5. 在本地上已经安装了 Python MySQLdb 模块。
#######################################################


#######################################################
#                    数据库查询操作                      #
#######################################################


# Python查询Mysql使用 fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据。
# fetchone(): 该方法获取下一个查询结果集，结果集是一个对象。
# fetchall():接收全部的返回结果行。
# rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。

# import the libs you want to use
import MySQLdb

print "========================="
print "     Hello, Python!      "
print "========================="


# 打开数据库连接
db = MySQLdb.connect("localhost","root","","TESTDB" )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > '%d'" % (1000)

try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
      # 打印结果
      print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
             (fname, lname, age, sex, income )
except:
   print "Error: unable to fecth data"


# 关闭数据库连接
db.close()
