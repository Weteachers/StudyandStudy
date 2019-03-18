# 1.查看CPU
- 1.1 查看CPU个数
  - cat /proc/cpuinfo | grep "physical id" | uniq | wc -l
  - **uniq命令：删除重复行;wc –l命令：统计行数**
- 1.2 查看CPU核数
  - cat /proc/cpuinfo | grep "cpu cores" | uniq
    - cpu cores : 4
- 1.3 查看CPU型号
  - cat /proc/cpuinfo | grep 'model name' |uniq
  - model name : Intel(R) Xeon(R) CPU E5630 @ 2.53GHz  
- 总结：该服务器有2个4核CPU，型号Intel(R) Xeon(R) CPU E5630 @ 2.53GHz

# 2.查看内存
- 2.1 查看内存总数
  - cat /proc/meminfo | grep MemTotal
  - MemTotal: 32941268 kB //内存32G

- 下面是一些命令的集合，供参考：
  - uname -a # 查看内核/操作系统/CPU信息的linux系统信息  
  - head -n l /etc/issue # 查看操作系统版本  
  - cat /proc/cpuinfo # 查看CPU信息  
  - hostname # 查看计算机名的linux系统信息命令  
  - lspci -tv # 列出所有PCI设备   
  - lsusb -tv # 列出所有USB设备的linux系统信息命令  
  - lsmod # 列出加载的内核模块   
  - env # 查看环境变量资源  
  - free -m # 查看内存使用量和交换区使用量   
  - df -h # 查看各分区使用情况  
  - du -sh # 查看指定目录的大小   
  - grep MemTotal /proc/meminfo # 查看内存总量  
  - grep MemFree /proc/meminfo # 查看空闲内存量   
  - uptime # 查看系统运行时间、用户数、负载  
  - cat /proc/loadavg # 查看系统负载磁盘和分区   
  - mount | column -t # 查看挂接的分区状态  
  - fdisk -l # 查看所有分区   
  - swapon -s # 查看所有交换分区  
  - hdparm -i /dev/hda # 查看磁盘参数(仅适用于IDE设备)   
  - dmesg | grep IDE # 查看启动时IDE设备检测状况网络  
  - ifconfig # 查看所有网络接口的属性   
  - iptables -L # 查看防火墙设置  
  - route -n # 查看路由表   
  - netstat -lntp # 查看所有监听端口  
  - netstat -antp # 查看所有已经建立的连接   
  - netstat -s # 查看网络统计信息进程  
  - ps -ef # 查看所有进程   
  - top # 实时显示进程状态用户  
  - w # 查看活动用户   
  - id # 查看指定用户信息  
  - last # 查看用户登录日志   
  - cut -d: -f1 /etc/passwd # 查看系统所有用户  
  - cut -d: -f1 /etc/group # 查看系统所有组   
  - crontab -l # 查看当前用户的计划任务服务  
  - chkconfig –list # 列出所有系统服务   
  - chkconfig –list | grep on # 列出所有启动的系统服务程序  
  - rpm -qa # 查看所有安装的软件包   
  - cat /proc/cpuinfo ：查看CPU相关参数的linux系统命令  
  - cat /proc/partitions ：查看linux硬盘和分区信息的系统信息命令   
  - cat /proc/meminfo ：查看linux系统内存信息的linux系统命令  
  - cat /proc/version ：查看版本，类似uname -r   
  - cat /proc/ioports ：查看设备io端口  
  - cat /proc/interrupts ：查看中断   
  - cat /proc/pci ：查看pci设备的信息  
  - cat /proc/swaps ：查看所有swap分区的信息  
- 2.2 查看内存条数

```
# dmidecode |grep -A16 "Memory Device$"

Memory Device

Array Handle: 0x1000

Error Information Handle: Not Provided

Total Width: 72 bits

Data Width: 64 bits

Size: 2048 MB //1条2G内存

Form Factor: DIMM

Set: 1

Locator: DIMM1

Bank Locator: Not Specified

Type: DDR2

Type Detail: Synchronous

Speed: 667 MHz

Manufacturer: 7F7F7F7F7F510000

Serial Number: 0403E324

Asset Tag: 450721

Part Number: 72T256220HR3SA

--

Memory Device

Array Handle: 0x1000

Error Information Handle: Not Provided

Total Width: 72 bits

Data Width: 64 bits

Size: 2048 MB //1条2G内存

Form Factor: DIMM

Set: 1

Locator: DIMM2

Bank Locator: Not Specified

Type: DDR2

Type Detail: Synchronous

Speed: 667 MHz

Manufacturer: 7F7F7F7F7F510000

Serial Number: 0403E324

Asset Tag: 450721

Part Number: 72T256220HR3SA

--

Memory Device

Array Handle: 0x1000

Error Information Handle: Not Provided

Total Width: 72 bits

Data Width: 64 bits

Size: No Module Installed //1个内存空槽

Form Factor: DIMM

Set: 2

Locator: DIMM3

Bank Locator: Not Specified

Type: DDR2

Type Detail: Synchronous

Speed: Unknown

Manufacturer:

Serial Number:

Asset Tag:

Part Number:

--

Memory Device

Array Handle: 0x1000

Error Information Handle: Not Provided

Total Width: 72 bits

Data Width: 64 bits

Size: No Module Installed //1个内存空槽

Form Factor: DIMM

Set: 2

Locator: DIMM4

Bank Locator: Not Specified

Type: DDR2

Type Detail: Synchronous

Speed: Unknown

Manufacturer:

Serial Number:

Asset Tag:

Part Number:

--

Memory Device

Array Handle: 0x1000

Error Information Handle: Not Provided

Total Width: 72 bits

Data Width: 64 bits

Size: No Module Installed //1个内存空槽

Form Factor: DIMM

Set: 3

Locator: DIMM5

Bank Locator: Not Specified

Type: DDR2

Type Detail: Synchronous

Speed: Unknown

Manufacturer:

Serial Number:

Asset Tag:

Part Number:

--

Memory Device

Array Handle: 0x1000

Error Information Handle: Not Provided

Total Width: 72 bits

Data Width: 64 bits

Size: No Module Installed //1个内存空槽

Form Factor: DIMM

Set: 3

Locator: DIMM6

Bank Locator: Not Specified

Type: DDR2

Type Detail: Synchronous

Speed: Unknown

Manufacturer:

Serial Number:

Asset Tag:

Part Number:
```
总结：该服务器有两条2G内存 ，空余4个插槽
# 3.查看硬盘
- 3.1 查看硬盘大小
  - fdisk -l | grep Disk
  - Disk /dev/cciss/c0d0: 146.7 GB, 146778685440 bytes
  - 总结：硬盘大小146.7G，即厂商标称的160G
