# 用户组

```
groupadd sexy   # 添加用户组sexy
cat /etc/group  # 查看group配置文件的内容

groupmod -n market sexy # 把sexy的组名改成market(新的组名称在前)
cat /etc/group

groupmod -g 668 market  # 把market用户组的编号改为668
cat /etc/group

groupadd -g 888 boss    # 创建一个叫做boss的用户组，并且编号为888
cat /etc/group

groupdel market # 删除market用户组（删除用户组之前，务必记得要删除用户组中的用户，否则就变成了系统的“黑户口”）
cat /etc/group
```

# 用户
```
groupadd sexy
useradd -g sexy tc1 # 向sexy用户组添加用户tc1
useradd -g sexy zz1 # 向sexy用户组添加用户zz1
useradd -d /home/xxx imooc  # 在创建用户的时候，用-d的方式给用户创建文件夹，如果不使用-d申明，默认就是用户名的文件夹，在/home目录之下；这里在创建imooc用户的时候，没有说明其用户组，系统会为imooc分配一个和imooc同名的用户组
usermod -c hot_tangcong tc1 # 给tc1用户添加注释hot_tangcong

usermod -l tc2 tc1  # 修改用户名，把新的用户名写在前面，原来的用户名在后，把tc1改为tc2
usermod -d /home/tc2 tc2    # 修改tc2个人文件夹的路径

uesermod -g sexy imooc  # 把imooc从默认的imooc用户组移动到sexy这一用户组

userdel zz1 # 删除用户zz1的账号
userdel -r zz1  # 删除用户zz1的账号，连同个人文件一起删除

touch /etc/nologin  # 禁止除了root之外的其他用户登录服务器，文件的内容无关紧要，创建这个文件即可达到效果

```
