## why pyenv

### 起因
- bug: 8.5.9版不能在文本框中输入中文
  + 根据 wiki , Tk 是图形用户界面(GUI)工具包, Tkinter 是 Python 标准库, 也是调用 Tk 的接口, 或者说实际是 _tkinter 决定调用哪个版本的 Tk, 而由于系统自带的版本 Apple 8.5.9 bug, 需要下载
  + 而 Tk 与 Tcl(工具命令语言) 封装, 根据[python官方说明] (https://www.python.org/download/mac/tcltk/#apple-8-5-9)与[Tk 文档](http://www.tkdocs.com/tutorial/install.html), 需要升级对应版本的[ActiveTcl 8.5.18.0](http://www.activestate.com/activetcl/downloads)而不是最新版本
- 下载(.dmg)后 python 调用的依然是老版 
 
```python
$wish
% /usr/bin/python2.7
#: 或者进入 IDLE 执行
>>> import Tkinter
>>> Tkinter.Tcl().eval('info patchlevel')
'8.5.9'
``` 
但是 ActiveTcl 8.5.18 是确实安装了的(第一次安装的8.6.4, 之后又安装了8.5.18), 目录也是官方说的:

```
$ pwd
/usr/local/bin
$ ls -R
brew		tclsh		tclsh8.6	teacup	  wish8.5
tclselect	tclsh8.5	tclvfse	 wish     wish8.6
```
安装是成功的, 但是系统自带的 python import Tkinter 接口所调用的还是Tk 8.5.9 , 一进 idle 就看到那 warning... 可 CLI wish 就是`Tcl 8.5 & Tk 8.5 (8.5.18)`

到这里我有点混乱, 两个安装目录不同就阳光道独木桥了?? 基本没想过这种问题...    
  
杀了不少时间生命后, 又看到 brew 安装的 python Tk 就是新的,,,  
中间还看见了 build _tkinter.so,,,PYTHONPATH,,,云云 一些搞不懂的, 又没时间了...   
于是选择了不用思考答案的方法, 先绕过去......  

- pyenv 再下个版本的 python,  local 后接口调的 tk 确实是8.5.18了 ; 


总之模模糊糊的, 现在补遗, 重新捋捋 

### Q: OS x python Tkinter 接口接的是谁
-  A: Apple 版 Tk 8.5.9, 人家自己重编的...而 pyenv 下载的 python 就调用了自己下载的 8.5.18
-  过程: 

搜索`python import tkinter 8.5.18`, 发现很多 activestate 上类似的问题...问题...

> Pythons are currently built so that the Tkinter binary is hard-linked for an 8.5 Tcl. If ActiveTcl 8.5 isn't present, it will use the Apple Tcl 8.5   

- 所以没下载在 System目录, python/Tkinter 就无视了我下载的 TCL? 这 bug 也是 Apple 8.5.9 的?.. 为什么查看版本信息不把是 Apple 还是 ActiveTcl 显示出来呢!  
 
- 根据[5年前与问题斗争](http://community.activestate.com/forum/version-859-under-mac-os-x-am-i-getting-it)和[这么多年来依然...](https://community.activestate.com/node/17011)以及[python bug issue](http://bugs.python.org/issue4017) 用户给出的一种解决 :


```
cd(/)/System/Library/Frameworks/Tcl.framework/Versions/ 
ls
8.4 8.5 Current  
cd(home)/Library/Frameworks/Tcl.framework/Versions/
ls
8.5 8.6 Current 
``` 

- 替换 System 的旧版 Tcl.framework....这样实际 python 走老路把 8.5.18 当做 Apple 8.5.9 调用了 ,另官方的解决没用找到,只看到说明....
- 建立连接[^link]也失败:
`Operation not permitted` 
- 然后这时候才有意识, 有什么阻止了对根目录里的 Systerm 和 usr/bin 的改动.....(后来看到说是 osX 升级 rootless...用这个系统居然一点没想过关心下, 为何苦逼的根源)

[^link]: http://blog.got7.org/2010/01/b-macactivetcl.html   

- 一开始还想着应该可以改改写着加载哪个版本 Tk 的文件, 所以去找了 导入 module 的路线; 知道 import 自己的脚本时, python 会编译个 .pyc 文件
  + 于是就去找 Tkinter 的类似文件, 里面应该有说明

用`find 路径 -iname  "tkinter*"`找到了系统自带 python 和 pyenv 下载的版本中都有 

```
Tkinter.py
Tkinter.pyc
Tkinter.pyo
```
瞄了眼 Tkinter.py 发现它 import 了 _tkinter, 搜索没有 _tkinter 倒是找到`_tkinter.so`, 大概就是它决定调用了什么版本的 Tk,
系统 python:

```
/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload
$ otool -L _tkinter.so
_tkinter.so:
	/System/Library/Frameworks/Tcl.framework/Versions/8.5/Tcl (compatibility version 8.5.0, current version 8.5.9)
	/System/Library/Frameworks/Tk.framework/Versions/8.5/Tk (compatibility version 8.5.0, current version 8.5.9)
	/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1225.1.1) 
``` 
pyenv :

```
_tkinter.so:
	/Library/Frameworks/Tcl.framework/Versions/8.5/Tcl (compatibility version 8.5.0, current version 8.5.18)
	/Library/Frameworks/Tk.framework/Versions/8.5/Tk (compatibility version 8.5.0, current version 8.5.18)
	/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1225.1.1)
```

**请注意,明确调用模块路径的正确姿势:**

```
>>> import _tkinter
>>> #: print _tkinter
>>> print _tkinter.__file__
/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload/_tkinter.so
```   

好了, 到 _tkinter.so, 没辙了... setup.py? 哪个 setup.py 决定调用的 _tkinter.so?... 好多个 setup.py...

### 系统自带的 python 无法指望了, 请安装 pyenv

- pyenv 可以使你在任意目录下切换任意版本
- 重要的是绕过 Apple Tk 的 bug, 这是你乐意的方式吧

- 安装姿势 (另有[installer](https://github.com/yyuu/pyenv-installer) 这个安装同时也安装了pyenv-virtualenv, 另不用编辑 .bash/profile, 都可以, 还有很多别的方式), 首次接触 profile 文件....

```
$git clone https://github.com/yyuu/pyenv.git ~/.pyenv
$vim .bash_profile
# :写入以下四行(ZZ 保存退出)
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$HOME/.pyenv/bin:$PATH"
export PATH="$HOME/.pyenv/shims:$PATH"
eval "$(pyenv init -)"
# :pyenv github给的, 还不知道 shims 是啥, 选这个吧
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

- 现在就能使用了, `pyenv help`查看帮助 , 对于当前问题迫切使用:
  + `pyenv --list` 查看可下载的版本
  + `pyenv install 版本` 下载
  + `pyenv rehash` 每次下载后执行
  + `pyenv local 版本` 设定当前路径下使用哪版; `pyenv local --unset` 取消
  + `pyenv version(s)` 显示当下版本, 加 s 为列出所有版本, * 标示当前所用
  + ...
- 另外也顺便安装下 pyenv-pip-rehash

```
git clone https://github.com/yyuu/pyenv-pip-rehash.git ~/.pyenv/plugins/pyenv-pip-rehash
```
每次 pip 安装包后会自动刷新吧..( 现在大概这么理解 rehash)

### ...