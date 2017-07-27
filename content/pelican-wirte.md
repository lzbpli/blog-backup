Title: 使用pelican写博客
Date: 2017-7-24 
Category: pelican
authors: ikerbo


# 使用pelican写博客

## 写博客

在content下面创建一个文件pelican-wirte.md
``` Markdown
Title: My First Review
Date: 2010-12-03 10:20
Category: Review

Following is a review of my favorite mechanical keyboard.
```
## 生成博客

博客写好之后还不能进行访问，需要把写好的博客转化为html代码，执行下面的命令进行生成
``` git
pelican content
```
生成的文件都在**output**目录里面，这些文件就是博客运行需要的静态文件。

上传博客

在命令行里面切换到output目录下面，git命令
``` git
cd ~/project/yoursite/output

git push
```

