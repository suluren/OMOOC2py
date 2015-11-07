# -*- coding: utf-8 -*-
#!/usr/bin/env python
# author: suluren

from bottle import route, template, request, run
from DateBook import reading, saving

#:url 映射代码, get 处理索取数据请求
@route('/')
def mydaily():
	new = request.GET.userinput
	if not new:
		return template('dailyweb', userdaily='hi~')
	else:
		saving(Filename, new)
		userdiary = reading(Filename)
		return template('dailyweb', userdaily=userdiary)

if __name__ == '__main__':
	Filename = 'daily.log'
	run(host='localhost', port=9090, debug=True, reloader=True)