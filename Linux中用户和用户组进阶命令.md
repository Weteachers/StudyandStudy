
```
passwd -l tc2   # 锁定用户tc2
passwd -u tc2   # 解锁用户tc2

passwd -d tc2   # 清除tc2的密码，这样tc2就可以无密码登录了
```

# 主要组与附属组
- 用户可以同时输入多个组
    - 一个主要组
    - 多个附属组

当一个用户属于多个组的时候，默认创建的文件是在主要组  
如果想以附属组的身份创建文件，就要把身份临时切换到附属组  
newgrp boss # 切换到附属组boss

```
gpasswd -a tc2 boss # 把tc2添加到boss用户组中，boss用户组是tc2的附属组（主要组依然是sexy）
gpasswd -d tc2 boss # 把tc2从boss组删除

useradd -g tc 3 group1 -G group2,group3,... # 添加用户的时候同时申明其主要组是group1，附属组是group2，group3...

gpasswd imooc   # 给imooc用户组设置组密码
```
