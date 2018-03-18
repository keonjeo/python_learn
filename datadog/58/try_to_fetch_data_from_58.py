#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
import MySQLdb
from lxml import etree
import MySQLdb

url='http://www.58.com/changecity.aspx?PGTID=0d202408-0000-1814-1956-f636ed802e20&ClickID=1'


html=requests.get(url).content

selector=etree.HTML(html)

province_data0=selector.xpath('//dd//a/text()')

province_data1=selector.xpath('//dd//a/@href')

data=zip(province_data0,province_data1)

n=1

for i in data:
    city_name=i[0]
    print "++++++++++++++++++++++++++++++++++++++++++++++++++++"
    print city_name
    print "++++++++++++++++++++++++++++++++++++++++++++++++++++"
    area=i[1].replace('http:','').strip()
    area = area.strip('//')

    if '-' in area:
        area=area.split('-')[1].replace('/','')
    else:
        area=area.split('.')[0]

    print "====================================================="
    print area
    print "====================================================="
    # conn=MySQLdb.connect(host='localhost',user='root',passwd='',db='TESTDB',port=3306,charset='utf8')
    # with conn:
    #     cursor=conn.cursor()
    #     print n,city_name, area,i[1]
    #     cursor.execute('insert into 58_area values (%s,%s,%s)',(n,area,city_name))
    #     conn.commit()
    #     n+=1


