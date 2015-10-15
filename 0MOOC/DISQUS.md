## DISQUS 

### 背景  
- disqus 能让你在个人网站里与别人交流，使用它会在网页底端出现一个评论区，每次打开你的 website，disqus 会自动加载；登陆disqus账户，你可以在评论框里输入，@别人，和社交网站差不多，也可以follow人

### 没有安装直接设置 
- 网上的教程大部分都要安装 gitbook、node.js、NPM 套件，后两个是什么不知道，第一个我就奇怪说他是命令行工具，为什么有 git 还要下载 gitbook？
  - 有个教程有步骤图，显示 gitbook 更像个图形化界面，本地 editor； 
- 我的目的是 git push 然后 github 和 gitbook 都齐活，gitbook 和 github 已经通过 webhooks连起来了； 
  - 所见教程最后一步都是设置 book.json
- 所以：不在本地预览，不需安装 NPM 套件，直接设置 book.json 即可；同样，不在本地使用图形化界面编辑图书也不用安装 gitbook，编辑 SUMMRAY.md 文件就能修改目录，进而编辑图书
	
		{
	    "plugins": ["disqus"],
	       "pluginsConfig": {
        "disqus": {
            "shortName": "example"
        }
	    }
		}
  - shortName 需要登陆 disqus 点击 Add Disqus to Site 设置（有Admin点Admin）再点击Engage 就可以编辑了；把 `.disqus.com` 前面那自己输入的部分填入 `"example"`就行；
  - 嗯……漏了`admin/settings/advanced/ `加`gitbook.com ``gitbook.io` 
  - 有个坑，看岔了 DAMA 给的模板 book.json（都是四行），以为 code 没问题，转而去找 disqus 设置的问题，找不到回来再看 code 才发现，真是活该没检查T.T




