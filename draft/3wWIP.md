### 3wWIP  

- User Datagram Protocol(UDP), wiki 也看不懂, 反而疑惑咋不用 TCP, 说是 UDP 丢包...先看看另一个吧

每张卡片都是 socket 库, 看了下末尾有 example, 有 bind 呐不过看不懂, 先搜搜 `socket`

两个程序(嗯,大妈是运行了2个 .py)通过双向通信连接实现数据交换(嗯, 日记内容..), 连接的两端都叫做 socket ;

- 一边是服务端(server), 另一边是客户端(client);
- 好了, 现在直奔官方文档, 搜索 udg...没明确的信息
- 看看 example, 创建 socket`socket(socket.AF_INET, socket.SOCK_STREAM)`
- 前者是internet, 后者是数据 TCL, 顺便查到了UDP 是 `SOCK_DGRAM`; 把例子改成 UDP, 却发现不支持 listen 和 accept...
- ok, 放弃文档, 不通用啊, 看看 [wiki.python](wiki.python.org/moin/UdpCommunication) 和 python howto
- udp 就 send, sendto, resv, resvfrom 用来发送接收, 没有连接.....