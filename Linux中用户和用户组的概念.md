# 用户和用户组
- 用户：使用操作系统的人
- 用户组：具有相同系统权限的一组用户

- /etc/group 存储当前系统中所有用户组信息
  - 每一行对应一个用户组的信息
  - 每一行都被分成4段
  - 如果组中用户名列表为空，单从这个配置文件来看，我们只能说这个用户组可能没有用户。因为这个用户组内只有一个用户，且用户名和用户组名相同，组内用户列表上是可以省略这个用户名的
  - 1.在Linux系统中，**root用户组的组号一定是0**
  - 2.组号1到499，属于系统预留的组编号，一般来说是预留给安装在操作系统中的软件或者服务的
  - 3.用户手动创建的用户组编号，从500开始，依次往后
  - 4.组密码占位符，无一例外，都是用一个x来表示
  
Group:|x:|123:|abc,def,xyz
---|---|---|---
组名称： | 组密码占位符：|组编号：|组中用户名列表

- /etc/gshadow 存储当前系统中用户组的密码信息  

Group:|*:|:|abc,def,xyz
---|---|---|---
组名称： | 组密码：|管理者：|组中用户名列表

- /etc/passwd 存储当前系统中所有用户的信息

usr:|x:|123:|456:|xxxxxx:|home/usr:|/bin/bash
---|---|---|---|---|---|---
用户名： | 密码占位符：|用户编号：|用户组编号:|用户注释信息:|用户主目录:|shell类型

- /etc/shadow 存储当前系统中所有用户的密码信息


