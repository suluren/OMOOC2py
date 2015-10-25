### GUI:图形用户界面  
桌面版日记系统, 视觉信息更丰富, 系统表达更友好

- 使用 Tkinter module: python 自带的 GUI 工具包 , 使用`import` 导入即可, 在 CLI python 解释器中试了下, 可以(python3 :tkinter)

```python
>>> import Tkinter
>>>           
#: 或者, 方便在于调用其中函数时前面不用声明Tkinter
from Tkinter import *   
```  
- how GUI, 安装 ActiveTcl 8.5.18? 那似乎也是种语言, 放着看 hello,Tkinter
  
```python
#: 创建了一个空窗口实例, 进入主循环, 关闭窗口, CLI 退出循环; 
变量名 = Tk()
变量名.mainloop()
```  
可以先倒腾下界面的代码  

- 代码是怎样的, 用到哪些函式? 需要定义一个类吗?  
  + Frame 创建框架, 放置文本框,按钮等部件 
  + Text 创建一个文本框部件, 用于输入日记和显示过往记录
  + button 创建两个按钮部件, 一个绑定保存写入文件命令(函式), 另一个绑定读取日记文件命令
  + pack 使部件在界面中可见
  + 打个比方, 类是神笔马良画在卷轴上的龙, 什么时候想要点个睛, 就从墙上飞出来了;
  + (不过龙飞出来之后, 卷轴上那只原始龙不会消失, 它具有所有龙最基本的属性和能力;)

- 界面是什么样  
  + 框架: `frame = Frame(master)`
  + 文本框: `text = Text(frame)`
  + 按钮: `w = Button(frame)`
  + run 了下 ,界面生成符合预想, 但是文本框不能输入中文, 输入只能显示字符, 但是复制张贴的中文好好地显示了.....搜索tk 文本框 中文输入, 似乎是需要升级安装下新tcl/tk ...但是那不是门别的语言吗? 先试试, 升级无用, 试了2个版本也无用
  + 看到有人和我一样遇到此坑, 决定也去 pyenv 下
- pyenv 无法下载 python ,重装 pyenv 后又可以了(并没有改变安装方法)
- 偏离主要问题如此长时间, 回头想我是不是应该先看看如何 get() 中文= =
- 发现类总是用不好, 顺着写吧(面向过程), 总觉得蹩手, 所以多用函数, 用类总忘了self... 写完作业再多练习练习

 ```
f.write('\n' + text) 
UnicodeEncodeError: 'ascii' codec can't encode characters in position 2-5: ordinal not in range(128)
```  

解决方法: 在 text 后加上.encode('utf-8'), 更多方法参考[这里](http://www.v2ex.com/t/163786)
- 搜索 text 发现 bind , 可以不用按钮了, 回车(事件参数)就能调用函数, 嗯, 既然cli 版日记使用 enter 完成一次输入, 我应该先搜搜 enter 才对..

- 接下来是, mainloop 起来就看到过往记录..
- 可以, 接下来把 filename 攒到总调下


  
