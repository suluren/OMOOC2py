## github 

### 重要功能  
- issue ：任何github用户都能在这里编辑，目前瞄到最多的 issue 到 #660；  
  - 以后可能需要用作分支名，比如 `git checkout -b issue-42` 这样，还不太了解分支，到时候用再说；
  - 个人仓库的 issue 在设置里开启  
- fork ：点击之后你也有一个一模一样的 repo 了  
- Pull requests ：向你 fork 的那个仓库的用户请求合并  
- 重要的大概就这三个，还有第四个的话就是 research 了，虽然目前只用它搜过 task

### 配置  
- SSH keys ：看到是说clone url 的方式会导致每次 push都要密码，现在不是不知道，感觉 github 迭代挺快， 保险还是设一下 SSH  
  - 0 检查本地有没有SSH keys `cd ~/.ssh`，有这个文件执行1   

  - 1 没有去执行2，再来执行1；有的话，执行 `cat id_rsa.pub` ，把终端显示的那段乱码复制粘贴到 github-Personal settings-SSH keys页面，点击 add SSH keys 就可以了
  - 2 没有就创建：`$ ssh-keygen -t rsa -C example@gmail.com `之后按提示操作，也可以一直回车，会采取默认设置	
  - 3 最后一步，检查成功与否：`ssh -T git@github.com`，出现 successfully authenticated 关键字就行
- webhooks：联动 github 与 gitbook——一边改动，另一边自动跟进  
fork仓库后，登陆（我使用github登陆）到 gitbook 页面创建 book；有四个选项，其中`GITHUB`和`IMPORT`效果一样：安装仓库目录 + 自动 add webhook
  - 二者也有区别，后者可从别的 git 托管方导入，格式：URL：`https://user:password@myserver.com/repo.git`    
 
  - 对应 github 也自动 webhook；进入 gitbook 的 book 页面 settings-github，点击check webhooks，一切正常就会跳转 github 的 webhooks  
  - webhook ：当特殊事件（比如 push）发生， webhooks 将通知对方；比如，在 gitbook 在线编辑时，新建文件后刷新 github 立即就有更新，文章内容编辑需保存后才更新      
 


