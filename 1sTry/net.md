## 每日笔记 net

### 使用 socket, 数据报(UDP)
> 神奇的插座,,,初印象:   
> 好像你处于上世纪打电话, 吼完一句对方不接茬, 继续大吼三句五句也没反应,
> 悻悻挂了, 后来问一句, 答: "刚听一句, xx掉了, 正趴地上摸呢, 起来你就挂
> 了, 你后来说啥了??"....

- 首先搜索 udp 是用户数据报协议, 把它理解为双方遵守固定的协约来传输数据; 至于其他, wiki 也只看懂 udp 相对 tcp 不可靠--会丢包, 但速度快, 任务在本地机子上就能完成, 也丢不到哪里去... 

- 那么 socket 是什么? 有许多理解:
 + 两个程序通过一个双向的通信连接实现数据的交换
 + 两个程序彼此通信的管道(倒是和阻塞匹配...)
 + 一种特殊的文件(函式用法非常像..)
 + .....

- 根据任务提示 socket 找到 example code, 意识到这句`s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)`切入在于`AF_INET SOCK_STREAM`;   

在文档中搜索知道前者是 address family 后者是 socket type, 依然不知道和 udp 什么关系, 文档搜索 'udp'和'protocol' 也没有用的信息... ok, 栗子不能用, 找其他...  

- 在[wiki.python](wiki.python.org/moin/UdpCommunication)总算明确 udp 的 socket type 是`SOCK_DGRAM`   
替换 tcp 却不能运行, udp 不支持 `listen` 和 `accept`, 那么支持那些呢? [看的例子](http://hackerxu.com/2014/11/28/python_socket.html)至少支持这些:  
`send sendto recv recvfrom connect`  

基本知道这些就够实现功能...

### C/S  

至于`(HOST, PORT)`, 这是一组**接口地址和端口号**的地址组合, 通常是指服务端的, 当然客户端也有

 - host, 说的就是 IP 地址, 网络中你的唯一标识
   + `'localhost'`or `'127.0.0.1'`: 适用仅在本地主机
   + `socket.gethostname()`return 当下主机名, 适用外网; 用 ipython 试试它能 bind 吗, 不行的话下面效果一样
   + `socket.gethostbyname(socket.gethostname())` : return 当下主机的 IP 地址
   + `s.getsockname()` return 本 socket 实例地址 , bind 前`('0.0.0.0', 0)/('::', 0, 0, 0)` 对应IPv4/v6; 用它检查下 bind 后地址
   + 此外, 还有 `''` 接受当下设备任何接口的连接

- port: 端口类型是 int, 虚拟端口, 物理接口;
  + 1024 以下是周知的, 比如 web server: 80, 本机运行建议4位到5位
  
- bind: 服务器将地址组与 socket 绑定, 即唯一标识(文件命名...), 客户端只要知道这组地址就能做到收发数据.....益rz   

知道地址的必要性, 现在可以开始写服务器和客户端两边的程序了  

- server 端
  + 创建 socket 对象, `s.bind((HOST, PORT))`
  + 接收`recv`, 返回数据和地址组 `recvfrom` , 调用就任性'blocked'(阻塞), 等他把数据返回之前进程不能干别的
  + 判断写入文件或是发送文件内容(复用)
  + 发送, `send` 由于已经连上, 不用指定地址 (即使用`sendto(massage, (HOST, PORT))`)
  + 循环以上 
  + 关闭, `s.close()`
  
- client 端
  + 创建 socket 对象, 不用 bind, 系统自动分配本身的 ip 和 端口组合
  + connect server
  + 进入收发循环, 输入笔记内容
  + `break` then `c.close()`
  
- 此外, 还需注意**同步**: 当程序执行到一个 recv 时, 没有数据发来就不会往下执行, 停在那里就像 raw_input 提示符在等待, 初印象来源于程序卡在此处

### 使用 select

- why select?  

> 当进行 `read` 或 `recv`, 只能等待一个连接, 如果有数倍的连接, 就必须
> 创建数倍的进程或线程(multi-process or multi-thread), 那是浪费系统
> 资源;

你在本机运行时, server 端收到的地址('127.0.0.1', xxxxx), xxxxx 就是系统开的进程, 每次运行 client 都没有重复的

> select 只需一个线程就能监视数倍连接; 当有数据变量时, 连接通信中就可以
>  call `read`或 `recv`   
> 可能一直阻塞, 或给定时限, 或不等, 取决于参数
> (第四个参数 timeout)
  
也就是说, 当有大量 socket 时, 需要非阻塞异步通信;  

- select 返回一个矩阵(包含三个列表和一个timeout)
  + 三个列表分别指输入事件、输出事件和异常事件, 当列表为空时, timeout 为 0 遇到阻塞立即返回不再等待..
  + 不懂这些事件怎么判断的, 使用上就把要处理的 socket 放进第一个列表
  + 当然也可以是 client socket
  + 由于只创建一个 server socket, 矩阵[0][0]就是他了
  + ....
  + 待完善

  
###小结 
- 这次没有死磕唯一的任务提示文档, 找了 python 的 wiki 和 howto 的例子入手, 只根据例子和调试也写出来了...
- 盲点在于不知道同步和阻塞: 
  + 打算客户端进入循环后发送读取请求时, 服务器在那边等着, 客户端在这边连输入提示符都没跳出来; 
  + 客户端进入循环了没发送, 服务器没接收数据, 后面循环语句都没有执行...
  
- 看了 alan lai 的笔记, 发现他先发送了请求关键字, 才想到这是一问一答游戏...
- 另, 每次复用代码, 都得改改才行, 以后得用起 return , 每次调用标准库的函式时, 不都*返回*了对象吗, ipython 用起来......
  
  
