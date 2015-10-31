# -*- coding: utf-8 -*-
#!/usr/bin/env python

import socket

HOST, PORT = 'localhost', 4242
#data = " ".join(sys.argv[1:])
help = '''\
          h|help|? : 打印帮助
          q|quit|exit : 退出每日笔记
       '''

sc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#: 连接服务器
sc.connect((HOST, PORT))
sc.send('r')
#sc.recv(10240)
print sc.recv(10240)

while True:  
    line = raw_input(">")
    if line in ['help', 'h', '?']:
        print help
    elif line in ['quit', 'q', 'exit']:
        print '嗯!(¦3[▓▓].....'
        break
    elif not line:
        continue
    else:
        sc.send(line)
        
