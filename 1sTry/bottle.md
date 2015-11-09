## webframe
> 每日笔记内网版(web 应用软件)  
> 与 net 版不同, 此次要求通过网页访问  
> task 提示: bottle

框架是什么? 要理解它看他主要干什么
   
- 如 Tk 也是框架, 它把一堆组件排布呈现出界面; 绑定一段处理代码与 GUI 上某项预定行为(比如在文本框 hit enter), 当我在界面触发时, 此段代码就会被执行(比如我要求他在指定组件插入内容)      
- 这两件事情, 就是 Tk 要做的; 那么 web 框架呢, 加上考虑数据传输是否可以同理推这两件事情?   
 + 排布网页传送给浏览器呈现 
 + 绑定 code 与某项用户触发的网页   

接下来就可以使用 bottle 开始建 web 应用, 验证对框架的想法

### 使用 bottle -- Python Web Framework
为什么用 bottle?  
在所有[webframe for python](https://wiki.python.org/moin/WebFrameworks/)里 bottle 是目前最小的 (python)WSGI web框架, 首先安装: `pip install bottle` ;   
也由于它太小了, 推荐用`wget`或`curl` 直接下载 [bottle.py](https://raw.githubusercontent.com/bottlepy/bottle/master/bottle.py) 放在项目目录里, 更多见 [文档](http://bottlepy.org/docs/dev/index.html)   

浏览教程, [Example: “Hello World” in a bottle](http://bottlepy.org/docs/dev/index.html)和[HTTP REQUEST METHODS](http://bottlepy.org/docs/dev/tutorial.html#http-request-methods)入手得出:

- `return` 数据就在浏览器呈现了
- `run()`  frame 生效, `debug(True), reloader=True`不用重运行程序
- 最重要的两件事得到印证: 
  + `template()`模板完成排布, `{{name}}, name=lisa`似格式化字符(%)
  + `@route()`完成代码与网页(此指 url)的绑定, 或者说映射
  + 关于框架需要更多解释, [参考这里](http://www.cnblogs.com/hazir/p/what_is_web_framework.html)
   
`return`的数据是 html 文件(即网页), 网页右键查看网页源代码显示的都很巨幅, 不可能都塞在 server 程序里;   
其间搜到 bottle 的完整实践: 通讯录和 todolist, 是将模板保存为 tpl 文件, template 不用后缀只用文件名就能调用, 保存在当前目录或其子目录 `views` 下都可以, 推荐后者    

那么浏览器如何传送 html文件 到 server 程序?   
对比上周, 无论数据复不复杂, socket 是一对 `send&recv`就搞定了, web 应用只有一边 server 程序如何识别获取以及反馈指定区域的数据?

- 浏览器与 server 程序以`request-response`模式交互
  + 浏览器请求, 能触发的操作很单纯, 基本只有点击和 enter
  + server 程序通过`request.<args>.get`获悉然后响应
  + `request.GET.get('a', '').strip()` 返回名为 a 的 get 参数 (parameter); 如果参数没有提交，返回一个空的字符串, strip() 默认去除首尾空格
  + 使用 `get()` 是以字典取值, 返回原始字符(byte string) , 引发过 `KeyError`  
  + 最好使用 `request.<args>.getunicode('<name>')`或`request.<args>.<name>`, 返回 Unicode string

- 发送请求是用 get 还是 host
  + 2种方法的功能范围不以名称所述划分, 取决于 handler code
  + 只是用法上, 当前 action 将改变应用时, 建议 host (比如用户创建账户)
  + get 方法最好只是响应对数据的请求  
  
接下来只剩模板了, 用 html 语言来写, 很简单

### 写模板  
可以参考[w3c html 教程](http://www.w3school.com.cn/html/index.asp), 不过知道了形式是这样: `<tag>显示内容</tag>`(显示内容被成对的尖括号包起来)  
就可以找个网页直接 copy 网页源代码做删减, 正好 [有个简单合适的](view-source:http://try.docopt.org/) , 复杂的 tag 要用再去看看手册

写完运行起来, 用 `curl -v url` 查看状态

--

ps: 最近两周任务区别可以近似看成需要考虑数据传输的 CLI 与 GUI...  
pps: restful风格, 待 dig...木有想到会搜出论文 orz


