#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys
from bs4 import BeautifulSoup
import urllib2
import time
import cookielib
cookJar = cookielib.CookieJar()
httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler, httpsHandler,urllib2.HTTPCookieProcessor(cookJar))
urllib2.install_opener(opener)

def find_last(string,str_a):
	last_position = -1
	while True:
		position=string.find(str_a,last_position+1)
		if position == -1:
			return last_position
		last_position=position

def getFigure(idx):	
	url = link['href']
	n_start=url.find("i")
	n_end=url.find("u/")
	imgurl=url[:n_start] + url[n_end:] + "?imageView2/0/w/640"
	refererurl=url

	request = urllib2.Request(imgurl)
	request.add_header('Host','tu303.com')
	request.add_header('Connection','keep-alive')
	request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36')
	request.add_header('Accept','image/webp,image/apng,image/*,*/*;q=0.8')
	request.add_header('Referer',refererurl)
	request.add_header('Accept-Encoding','gzip, deflate')
	request.add_header('Accept-Language','zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7')
	request.add_header('Cookie','UM_distinctid=166200f602e187-0e92c42446fb06-43450521-100200-166200f602f7e1; CNZZDATA1261147851=2012588244-1538136091-%7C1538360698')
	response=urllib2.urlopen(request)
	file_n=find_last(url,'/')
	#print file_n

	fileName=url[file_n + 1:]
	f = open(fileName,"w")
	f.write(response.read())
	f.close()

#	print response.read()	
def constructRequest(i):
	url = "http://x771201.com/bbs/read.php?tid=1696068"
	request = urllib2.Request(url)
	request.add_header('Host','x771201.com')
	#request.add_header('Connection','keep-alive')
	#request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36')
	#request.add_header('Accept-Encoding','gzip, deflate')
	#request.add_header('Accept-Language','en;q=0.8,zh-TW;q=0.7')
#timeStamp=time.time();
#cookieStr='4bd54_ol_offset=284404; 4bd54_readlog=%2C1696068%2C; 4bd54_c_stamp='+str(timeStamp)+'; 4bd54_lastpos=index; 4bd54_lastvisit=318%091539420106%09%2Fbbs%2Findex.php; sc_is_visitor_unique=rx4629288.1539420074.400E44B76E054FB8C19B80ADE5F5F0F8.1.1.1.1.1.1.1.1.1'
#request.add_header('Cookie',cookieStr) #'Cookie:4bd54_ol_offset=284404; 4bd54_readlog=%2C1696068%2C; 4bd54_c_stamp=1539420106; 4bd54_lastpos=index; 4bd54_lastvisit=318%091539420106%09%2Fbbs%2Findex.php; sc_is_visitor_unique=rx4629288.1539420074.400E44B76E054FB8C19B80ADE5F5F0F8.1.1.1.1.1.1.1.1.1')
	content = urllib2.urlopen(request).read()
	#print content
	f = open(str(i),"w")
	f.write(content);
	f.close()
#
for i in range(7,15): 
	constructRequest(i)
	time.sleep(1)
#f = open("php.html","w")
#f.write(content);
#f.close()
#print content
#soup = BeautifulSoup(content,"html")
#soup = BeautifulSoup(open('read.php?tid=1690333'),"html")
#soup = BeautifulSoup(open('1.html'),"html")
#for child in soup.body.children:
#    print child

#start to get image
#soup = BeautifulSoup(content,"html")
#container = soup.body.select('#read_tpc')
#n=1
#for link in container[0].find_all('a'):	
#	print link['href']
#	print "try\n"
#	getFigure(n)
#	n = n+1


