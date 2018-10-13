#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys
from bs4 import BeautifulSoup
import urllib2
import time

class RedirctHandler(urllib2.HTTPRedirectHandler):
	"""docstring for RedirctHandler"""
	def http_error_301(self, req, fp, code, msg, headers):
		pass
	def http_error_302(self, req, fp, code, msg, headers):
		pass


httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
#redirectHandler = urllib2.HTTPRedirectHandler()
opener = urllib2.build_opener(httpHandler, httpsHandler,RedirctHandler)
urllib2.install_opener(opener)

	
url = "http://x771201.com/bbs/link.php?action=previous&fid=6&tid=1696068&fpage=0&goto=previous"
request = urllib2.Request(url)
request.add_header('Host','x771201.com')

request.add_header('Connection','keep-alive')
request.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36')

request.add_header('Accept-Encoding','gzip, deflate')

request.add_header('Accept-Language','zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7')

request.add_header('Referer','http://x771201.com/bbs/read.php?tid=1696068')

timeStamp= time.time() # add time stamp

cookieStr='4bd54_ol_offset=284404; 4bd54_readlog=%2C1696068%2C1696267%2C; 4bd54_c_stamp='+str(timeStamp) + '4bd54_lastpos=other; 4bd54_lastvisit=2079%091539421867%09%2Fbbs%2Fhitcache.php%3Ftid1696267; sc_is_visitor_unique=rx4629288.1539429948.400E44B76E054FB8C19B80ADE5F5F0F8.2.2.2.1.1.1.1.1.1'

request.add_header('Cookie',cookieStr)


content = urllib2.urlopen(request).read()
#f.close()
print content
