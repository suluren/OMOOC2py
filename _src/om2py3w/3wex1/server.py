# -*- coding: utf-8 -*-
#!/usr/bin/env python
# author: suluren

import socket, select
import sys
import DateBook

HOST, PORT = 'localhost', 4242
bufsize = 10240
#: AF_INET: Ipv4; SOCK_STREAM: TCP, SOCK_DGRAM: UDP
ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print '服务端创建'
#:socket.gethostname()可访问外界; localhost 限同台机, 第二个参数建议4, 5位
ss.bind((HOST, PORT))
print '绑定主机与端口'
ss.setblocking(0)

while True:
	result = select.select([ss],[],[])
	data, remote_addr = result[0][0].recvfrom(bufsize)
	print "收到{}请求".format(remote_addr)
	if data == 'r':
		diary = DateBook.reading('daily.log')
		ss.sendto(diary, remote_addr)
	elif data == 'q':
		print "客户端{}已退出".format(remote_addr)
		a = raw_input("是否继续, 'y' 继续, 任意字符退出")
		if a == 'y': 
			 continue
		else: break

	else:
		print "来自{}的数据:{}".format(remote_addr, data)
		DateBook.save('daily.log', data)

ss.close()