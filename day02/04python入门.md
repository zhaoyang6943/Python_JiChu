# python入门

[TOC]

------

### 1.python语言介绍

编程语言介绍

机器语言

​	二进制，计算机是电启动的，电有什么特性，计算机就有什么特性。

汇编语言

​	和机器语言半斤八两。。

高级语言（编译性、解释性）

​	按照翻译的方式不同，分为两种！
​	编译性，C；编译器，谷歌翻译的软件，最终翻译成机器语言

​	解释性，python； 解释器，解释一行，执行一行。

​	一系列复杂的翻译的细节，屏蔽了大量的计算机底层的东西。

![1616070221987](C:\Users\八块腹肌\AppData\Roaming\Typora\typora-user-images\1616070221987.png)

​	编程语言分类，总结

### 2.python介绍

python的语法风格
还是python的解释器？

确定语法风格，然后编写python解释器！解释器多强大，软件运行就有多高！Cpython的解释器。C语言的解释器。

python的发展历史，就是python解释器的发展史！

### 3.解释器多版本共存

设置环境变量

​	windows

​		win10：写在前面的先执行；可以通过命名方式的不同，执行不同版本的python

​		win7：就一条环境变量，设置前面的先执行

​	linux：

​		vim /etc/profile

​			PATH=$PATH:/usr/loacl/python38:/usr/local/python39

​			export PATH

### 3.linux下安装python

cat /etc/redhat-release

命令解释：查看linux环境版本

```shell
[root@hecs-x-large-2-linux-20210314214122 ~]# cat /etc/redhat-release
CentOS Linux release 7.6.1810 (Core)
```

```shell
[root@hecs-x-large-2-linux-20210314214122 tmp]# ll
total 12
drwxr-xr-x 2 root root 4096 Mar 14 21:49 hsperfdata_root
drwx------ 3 root root 4096 Mar 14 21:46 systemd-private-4484e11129174f0b96bc090d59c60f5c-chronyd.service-vkGbq1
drwx------ 3 root root 4096 Mar 14 21:49 systemd-private-e659e02e1bd34e0da9537875179923fc-chronyd.service-JxFVd9
prw-r--r-- 1 root root    0 Mar 14 21:49 wrapper-645-1-in
prw-r--r-- 1 root root    0 Mar 14 21:49 wrapper-645-1-out
prw-r--r-- 1 root root    0 Mar 18 22:27 wrapper-670-1-in
prw-r--r-- 1 root root    0 Mar 18 22:27 wrapper-670-1-out
[root@hecs-x-large-2-linux-20210314214122 tmp]# cd 
[root@hecs-x-large-2-linux-20210314214122 ~]# ls
1.log  2.log  log.txt  nginx.log  Python-3.8.8.tgz  Python-3.9.2.tgz
[root@hecs-x-large-2-linux-20210314214122 ~]# tar xvf Python-3.8.8.tgz -C /tmp/
```

解释：解压到tmp文件夹内：

`tar xvf Python-3.8.8.tgz -C /tmp/`



```shell
[root@hecs-x-large-2-linux-20210314214122 ~]# cd /tmp/
[root@hecs-x-large-2-linux-20210314214122 tmp]# ll
total 16
drwxr-xr-x  2 root root 4096 Mar 14 21:49 hsperfdata_root
drwxr-xr-x 17 1000 1000 4096 Feb 19 19:04 Python-3.8.8
drwx------  3 root root 4096 Mar 14 21:46 systemd-private-4484e11129174f0b96bc090d59c60f5c-chronyd.service-vkGbq1
drwx------  3 root root 4096 Mar 14 21:49 systemd-private-e659e02e1bd34e0da9537875179923fc-chronyd.service-JxFVd9
prw-r--r--  1 root root    0 Mar 14 21:49 wrapper-645-1-in
prw-r--r--  1 root root    0 Mar 14 21:49 wrapper-645-1-out
prw-r--r--  1 root root    0 Mar 18 22:30 wrapper-670-1-in
prw-r--r--  1 root root    0 Mar 18 22:30 wrapper-670-1-out
[root@hecs-x-large-2-linux-20210314214122 tmp]# ./configure --prefix=/usr/local/python38
-bash: ./configure: No such file or directory
[root@hecs-x-large-2-linux-20210314214122 tmp]# cd Python-3.8.8/
[root@hecs-x-large-2-linux-20210314214122 Python-3.8.8]# ./configure --prefix=/usr/local/python38
```

解释：到tmp下的python38文件内去，安装python3.8，安装路径一般是/usr/local下；



```shell
creating Modules/Setup.local
creating Makefile

If you want a release build with all stable optimizations active (PGO, etc),
please run ./configure --enable-optimizations

[root@hecs-x-large-2-linux-20210314214122 Python-3.8.8]# make && make install
```

解释：编译并安装



执行python3的时候，如果不是自己想要的python版本，使用命名`which python3`就会将当前执行的python3版本路径显示出来，对应找python3的版本。

直接执行python3命令 并不会执行当前目录下的python3
./python3才是执行当前目录下的python3；跟自己的环境变量有关系，python3执行的顺序有关系。



### 4.请去自己了解pyenv

为了效率不可能一直去手动修改环境变量，去到对应的python环境；所以直接使用pyenv



### 5.运行python程序的两种方式

##### 1.交互式

即时得到程序的运行结果，多用于调试

##### 2.脚本的方式

把程序写到文件里（约定俗称文件后缀为.py）,然后用python解释器解释执行其中的内容



python3.8 python程序文件的路径

### 6.一个python应用程序的运行的三个步骤（六星）

python3.8 C:\a\b\c.py

**1.**先启动python3.8解释器，此时相当于启动了一个文本编辑器

**2.**解释器会发送系统调用，把c.py的内容从硬盘读入内容，此时c.py中的内容全部为普通字符，没有任何语法意义

**3.**解释器开始解释执行刚刚读入内存的c.py的代码，开始识别python语法



对比文本编辑器读取C:\a\b\c.py文件内容也经历了三个步骤

1.先启动文本编辑器

2.文本编辑器会发发送系统调用，把c.py的内容从硬盘读入内存

3.文本编辑会将刚刚读入内存的内容控制输出到屏幕上，让用户看到结果



总结：

二者在前两个阶段做的事情完全一致

唯一不同的就是第三个阶段对读入内存的python代码的处理方式不同



### 7.集成开发环境介绍

pycharm

环境，提升开发效率



### 8.注释

对代码的解释说明

被注释的代码不会被执行



### 9.考试10分钟：

1.机器语言、汇编语言、编译型、解释性语言在执行效率、开发效率、跨平台性方面的高低对比



2.python解释器与python语言的关系

​	python解释器是一款应用程序，专门用来解释执行python这门语言风格并执行；

​	python语言编写的程序最终都是被解释器执行的，所以我们可以这么说Python语言更多的都是在调用Python解释器的功能，所以解释器性能的高低，很大程度就决定了python语言的运行效率

3.什么是环境变量PATH，或者说它是用来干什么的？

​	如果想在任何情况都能执行python.exe就需要环境变量

4.运行python程序的两个方式

​	交互式，一定要写python语法。。不要敲pip命令

​	脚本的方式，写到文件存储

5.一个python程序运行的三个步骤/阶段

​	总结它与文本编辑器读取文件的三个阶段的相同之处与不同之处

​	a，python解释器启动

​	b，python解释器把a.py的内容当做普通的文本内容，由硬盘读入内存（本质是解释器向操作系统发起系统调用，让操作系统控制硬件完成读取）

​	c，解释器解释执行刚刚读入内存的python代码，开始识别python语法

6.注释的种类、注释的用途

​	单行注释

​	多行注释

​	1.解释说明

​	2.不执行代码