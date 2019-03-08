# coding = utf-8

import os

if os.getuid() == 0:
	pass
else:
	print("当前用户不是root用户，请以root用户执行脚本")
	sys.exit(1)

version = raw_input('请输入你想安装的python版本(2.7/3.5)')
if version == '2.7':
	url = 'https://www.python.org/ftp/python/2.7.12/Python-2.7.12.tgz'
elif version == '3.5':
	url = 'https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz'
else:
	print("您输入的版本号有误，请输入2.7或者3.5")
	sys.exit(1)

cmd = 'wget'+url
res = os.system(cmd)
if res	
