### 使用 pip 下载管理第三方包
既然已装 pyenv 和 pyenv-pip-rehash, 就来试试怎么用 pip 吧

- 使用前先更新(在 pyenv 设置的 python 环境下执行), 当前是6.1.1, 更新后是 7.1.2

```
pip install --upgrade pip
或者
pip install -U pip
```

- 几个命令
  + `pip install <Package>` 下载包
  + 指定版本, 比如:`pip install ipython==4.0.0` 
  + 更新包, 你已经看过啦
  + `pip uninstall <Package>` 卸载包
  + `pip list` 列出你的第三方包名字及版本
  + `pip show <Package>` 显示包的详细信息, 当然 pip 自己也是

### 使用 ipython  

ipython 比 idle 更好用, 原生 shell....  
刚刚已经安装, 输入 ipython 进入, 自动 rehash 了 


- 交互: [in][out] , 不用 print, 每行代码只要有输出, 直接显示
