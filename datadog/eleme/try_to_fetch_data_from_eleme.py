#!/usr/bin/env python
# -*- coding: UTF-8 -*-

print "#############################################"
print "#              Hello, Python!               #"
print "#############################################"

import requests
import json
import MySQLdb
import sys

reload(sys)
sys.setdefaultencoding('utf8')

url='https://mainsite-restapi.ele.me/shopping/v1/cities'

html=requests.get(url).content
json_data=json.loads(html)
city_code=json_data


file = open("datadog/eleme/data/cities.csv", "w+")

# file.write("www.runoob.com!\nVery good site!\n")
# hello = "hello"
# world="world"
# file.write(hello + " " + world + "!\n")



file.write("Id,Code,City Name,City Abbr,Longitude,Latitude.City PinYin\n")

for code in city_code:
  city_info=json.loads(html)[code]
  for city in city_info:
    print "=========================================================================================="
    print city['id'],code,city['name'],city['pinyin'],city['abbr'],city['longitude'],city['latitude']
    file.write(str(city['id']) + "," + code + "," + city['name'] + "," + \
      city['abbr'] + "," + str(city['longitude']) + "," + str(city['latitude']) + "," + city['pinyin'] + "\n")
    print "=========================================================================================="
    # conn = MySQLdb.connect(host="localhost",user="root",passwd="",charset="utf8", db='TESTDB',port=3306)
    # with conn:
    #     cursor=conn.cursor()
    #     sql="insert into dim_eleme_area values(%s,%s,%s,%s,%s,%s,%s)"
    #     cursor.execute(sql,(code,city['name'].encode('utf8'),city['pinyin'],city['abbr'],city['longitude'],city['latitude'],city['id']))
    #     conn.commit()

# Close the file handler
file.close