# 课程目标
- 学会Ansible安装
- 学会运行Ansible
- 了解Ansible配置项

# 环境准备
- python
- Setuptools（python包）
- Pip(可选)

# Ansible快速安装
- 1.安装pip: easy_install pip
- 2.安装Ansible: pip install ansible

# Ansible源码安装
- 1.[获取源码](https://github.com/ansible/ansible)
- 2.解压源码
- 3.进入安装目录
- 运行source./hacking/env-setup

# Ansible系统源安装
- Centos
  - yum install ansible
- Ubuntu
  - apt-get install software-properties-common
  - apt-add-repository ppa:ansible/ansible
  - apt-get update
  - apt-get install ansible
  
  # Ansible运行
  Ansible-->ssh-->shell
  
  # Ansible配置文件路径
  - export ANSIBLE_CONFIG
  - ./ansible.cfg
  - ~/.ansible.cfg
  - /etc/ansible/ansible.cfg
  
  # Ansible配置文件获取
  - /etc/ansible目录下
  - https://raw.github.com/ansible/ansible/devel/examples/ansible.cfg
  
  # Ansible 配置详解
  - defaults 默认配置项（一般情况不需要修改）
    - ask_pass & ask_sudo_pass
    - ask_pass:可以控制，Ansible剧本playbook是否会自动默认弹出密码
    - ask_sudo_pass:用户使用的系统平台开启了sudo密码的话，应该开启这一参数(设置成true)
    - gather_subset
      - 信息手机的内容：包括all network hardware virtual facter ohai
    - remote_port&remote_tmp&remote_user
      - 客户机的设置，分别对登录的用户和端口，以及临时目录
    - sudo_exe & sudo_flags & sudo_user
      - sudo命令相关设置，分别是sudo命令路径、sudo参数、能够使用sudo的user
    - action_plugins& callback_plugins&connection_plugins & filter_plugins&lookup_plugins&vars_plugiins  
    
  - privilege_escalation 执行命令的用户权限设置
  - paramiko_connection paramika插件设置
  - ssh_connection ssh 连接设置
  - accelerate
  - selinux & colors
