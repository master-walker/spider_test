#!/usr/bin/env python
#coding=utf-8

'''
test
'''

import urllib
import urllib2
import codecs

# url = "http://www.163.com"
# request = urllib2.Request(url)
# response = urllib2.urlopen(request)
# # print response.read()
# with codecs.open("163.html", 'w+') as f:
#     # f.write(response)
#     print 2


'''
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding:gzip, deflate, br
Accept-Language:zh-CN,en-US;q=0.8,en;q=0.6,zh;q=0.4
Cache-Control:no-cache
Connection:keep-alive
Cookie:timeseed=1505879305; g_sid=lndukahjb0ou05oq8bl1nm2qi0; ie=0; summary_eid=1696473592-1434333061-; __asc=f195c9d915f52c3b68e73b6685d; __auc=f195c9d915f52c3b68e73b6685d; g_k_token=lndukahjb0ou05oq8bl1nm2qi0%40%7C878105b3b9916bdfebeaec1b2848b7ff; isLogin=1; loginSource=home; imSideBar=0; k=on
DNT:1
Host:www.gcall.com
Pragma:no-cache
Referer:https://www.gcall.com/?ref=logout
Upgrade-Insecure-Requests:1
User-Agent:Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36
'''

import cookielib

url = "https://www.gcall.com"
user_agent = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36"
values = {"username": "", "password": ""}
headers = {"User-Agent": user_agent}
data = urllib.urlencode(values)
request = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request)
print response.read()

#声明一个CookieJar对象实例来保存cookie
cookie = cookielib.CookieJar()
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib2.build_opener(handler)

response = opener.open(url)

for item in cookie:
    print "{0} {1}".format(item.name, item.value)
