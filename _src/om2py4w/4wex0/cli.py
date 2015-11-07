#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: suluren

import requests
from bs4 import BeautifulSoup


def main():
	while True:  
		line = raw_input(">")
		if line in ['quit', 'q', 'exit']: 
			break
		elif line in ['s', 'sync']:
			print syncrequest(URL)
		else:
			requests.post(URL, data={'userinput':line})
	    	

def syncrequest(url):
	#:获取网页到本地
	r = requests.get(url)
	#: bs 解析网页内容
	s = BeautifulSoup(r.content, 'html.parser')
	#: 返回标签 textarea 括起来的文本
	return s.textarea.get_text()

if __name__ == '__main__':
    help = '''\
              (๑•́ ₃ •̀๑)~使用帮助~
              q|quit|exit : 退出每日笔记
              s|sync : 读取笔记记录
           '''
    URL = 'http://localhost:9090/'
    print help
    main()
