# -*- coding: utf-8 -*-
#!/usr/bin/env python
# author: suluren

import socket, select
import sys

server_addr = ('', 4242)
bufsize = 8192

ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ss.bind(server_addr)
#: False, 非阻塞
ss.setblocking(0)

while 1:
	result = select.select([ss],[],[])
	msg, addr = result[0][0].recvfrom(bufsize)
	print "来自{}的数据:{}".format(addr, msg)
	if msg == 'q':
		break
	else: continue

ss.close()