# -*- coding: utf-8 -*-
#!/usr/bin/env python

import socket


HOST, PORT = 'localhost', 4242
#data = " ".join(sys.argv[1:])

sc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:  
    line = raw_input(">")
    if line in ['help', 'h', '?']:
        print '''\
                  (๑•́ ₃ •̀๑)~需要帮助? 很简单喔~
                  输入完一行回车, 日记就保存了, 下次进来就看到了~
                  '''
    elif line in ['quit', 'q', 'exit']:
        print '嗯!(¦3[▓▓].....'
        break
    elif not line:
        continue
    else:
        sc.sendto(line, (HOST, PORT))

#print '日记记录:', sc.recv(10240)
