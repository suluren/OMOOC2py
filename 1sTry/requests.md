> 今天旁观一个问题的始末, 再次认识: 问题的关键字在哪里, 不在未来&未知, 却是来路, 请描述之...  

## 获取网页&解析  
> task要求: 命令行操作与 webserver 交互  
> 原表述为兼容 3w net 版命令行界面交互  
     
意外联想: 试试直接打开客户端和 webserver , 这会儿写笔记试了下果然连接失败, 当然数据发送不过去, 管道没对上   
还有点啥线索呢? 1stry 里各种空教程名(可以得到关键字 `requests`)以及写完 web 应用, 这个 web 应用其实就是程序和浏览器对传数据: 请求&响应   
问 CLI 如何获取这个数据前先问: 你要获得的数据是什么呢? 和上周 socket 发来的数据有什么不一样? 写完 webserver, 已有答案

对传数据是网页, html 文件; 接下来的问题就是:  
如何获取网页并按自己的意愿处理网页(比如取出自己要的部分)    

### 使用 requests
requests是 python 的 HTTP 库, 诚如所述, 优雅简单, 4行完成 urllib2 两倍以上代码工作: 请求成功(response code 200)打印内容类型;  
  
那么安装: `pip` , [或者详见](http://requests-docs-cn.readthedocs.org/zh_CN/latest/user/install.html#install) 
 
ok, [进入文档](http://requests-docs-cn.readthedocs.org/zh_CN/latest/user/quickstart.html#id4), 第2句代码就解决怎么获取网页, 看见`>>>`就运行起 webserver 程序, 然后进入 ipython(或者idle), tail 文件, 快速上手  
  
```
r = requests.get("<url>")
#: bottle server
"GET / HTTP/1.1" 200 222
```
那么尝试发送数据, 使用字典比如`{'<name>':'helloworld'}`, 关键字[用 data 还是 param](http://stackoverflow.com/questions/24535920/difference-between-data-and-params-in-python-requests)? 大概是 post 请求或数据较大用 data; 使用`data`server 就没有显示query string 即 `?<name>=helloworld`这一段  
把 response 对象赋给 r, 要的网页就在里面了  
text 和 content 获取网页文本的区别: `r.text`得到 `Unicode string` , `r.content` 得到 `string`, 打印效果一样, 建议 content 
 
网页内容有了, 咋解析呢

### 使用 BeautifulSoup(bs4)  
> 文档: [中文](http://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/), [e 文](https://beautiful-soup-4.readthedocs.org/en/latest/#quick-start)  

google 搜索 python 解析网页 beautifulsoup 中文文档在第四个, 另python文档里搜索 html, 自带标准库有 HTMLParser, 可以覆写类来解析网页, 但不用他, 用第三方 bs4的原因同上; 

安装, 还是 pip, 其他见文档  

- 接着 ipyhon 折腾
  + 一部曲: 网页给它过滤遍 `soup = BeautifulSoup(r.content)`  
跳出了 userwarning: 未指明解析器, 当前使用 HTML 解析器(html.parser), 可能在其他系统或虚拟环境里, 会出现使用不同的解析器导致的差异...那就加上,,,(e 文文档 Quick Start 写了, 中文的没有...
  + 二部曲: 获取标签除外的文本 `get_text`, (另有`getText` 和 `get`, 没看出区别) ; 另发现变化`charset="unicode-escape"`不过没出现 bug, 不管  
  + 三部曲: 获取指名标签的文本内容 `<tag>.get_text` 
  + over
  + 以及文档还是英文的好, 一手源头, 中文文档往后翻了好多才发现指明标签, 虽然看见 get_text 就尝试出了有效代码... e 文在安装之前这三部曲就都写明了, 按照对象-标签-文本的顺序, 更自然...  



