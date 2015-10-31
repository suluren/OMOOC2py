# -*- coding: utf-8 -*-
#!/usr/bin/env python
# author: suluren

import socket
import sys
import DateBook

HOST, PORT = 'localhost', 4242
#: AF_INET: Ipv4; SOCK_STREAM: TCP, SOCK_DGRAM: UDP
ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print '服务端创建'
#:socket.gethostname()可访问外界, localhost 限同台机; 第二个参数建议4位
ss.bind((HOST, PORT))
print '绑定主机与端口'

while True:
	data, remote_addr = ss.recvfrom(10240)
	if data in ['read', 'r']:
		with open('daily.log') as readbook:
			diary = readbook.read()
	        ss.sendto(diary, remote_addr)
	else:
		print type(remote_addr)
		print "来自{}的数据:{}".format(remote_addr, data)
		DateBook.save('daily.log', data)
	#print '连接' + addr[0] + ':' + str(addr[1])

ss.close()