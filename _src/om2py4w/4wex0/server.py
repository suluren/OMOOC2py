#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: suluren

from bottle import route, template, request, run
from DateBook import reading, saving

#:url 映射代码, get 处理索取数据请求
@route('/')
def mydaily():
	userdiary = reading(Filename)
	return template('sync', userdaily=userdiary)

#: post 处理更新数据请求
@route('/', method='POST')
def syncnote():
	new = request.POST.userinput
	if new:
		saving(Filename, new)
	userdiary = reading(Filename)
	return template('sync', userdaily=userdiary)

if __name__ == '__main__':
	Filename = 'daily.log'
	run(host='localhost', port=9090, debug=True, reloader=True)