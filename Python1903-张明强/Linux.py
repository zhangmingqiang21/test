
python操作Linux系统
import paramiko
#第一步、连接Linux系统

#建立连接，创造一个sshclien对象  ,通过协议连接的
s = paramiko.SSHClient()

#建立连接第二步、允许信任Linux主机，类似于xshell第一次连接
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#建立连接的第三步、使用connect连接远程Linux主机
s.connect(
    hostname= "192.168.0.129",
    port = 22,
    username= "root",
    password="zmq123456"   #这个是登陆Linux系统的密码
)

#第二种连接Linux的方式
t = paramiko.Transport(('192.168.0.129',22))
t.connect(username='root',password='zmq123456')
sftp = paramiko.SFTPClient.from_transport(t)    #括号内是参数：一个套字节服务端口


第二个执行Linux命令
studin,stdout,stderr = s.exec_command("ls -al")    #exec_command("执行命令的方法")，命令要写成字符串的形式
print(stdout.read().decode())     #studin输入，stdout输出，stderr错误 ,decode解码

# #第三个、文件上传、下载    开启文件传输的端口号
# #创建一个文件传输通道，sftp客户端方法，
# # sftp = paramiko.SFTPClient(s)    #paramiko.SFTPClient(连接名)
# x1 = '/home/aaa.txt'    #Linux远程文件
# x2 = r'C:\Users\86157\Desktop\Python1903-张明强\py1.txt'   #保存到本地的位置
# # sftp.get(x1,x2)    #第一个远程文件，第二个本地文件

# #文件上传 第一个本地文件，第二个远程文件
# sftp.put(x2,x1)

import os
#os.path 类
#1返回文件的绝对路径
# b = os.path.abspath('A')
# print(b)

#返回文件的上一级目录名
# c = os.path.dirname(r'C:\Users\86157\Desktop\Python1903-张明强')
# print(c)

#返回文件当前的目录
# d = os.path.basename(r'C:\Users\86157\Desktop\Python1903-张明强')
# print(d)

#判断文件是否存在
# f = os.path.exists ("C:\\")
# print(f)

#判断是否为目录
# f  = os.path.isdir('A')
# print(f)

#判断是否为文件
# g = os.path.isfile('文件路径/文件名')
#
# #判断是否为连接文件
# h = os.path.islink('文件路径/文件名')
#
# #文件路径拼接
# j = os.path.join('/Users/','jio')
#
# #文件路径分离 ,将前一个文件/目录  和最后一个进行分割，返回一个元组
# k = os.path.split(r'C:\Users\86157\Desktop\Python1903-张明强')
# print(k)

#分割文件的后缀名
# l= os.path.splitext(r'C:\Users\86157\Desktop\Python1903-张明强')
# print(l)


a = input("输入账户:")
b = input("输入密码:")
if a == '12' and b =='11':
    print("正确")
else:
    print("错")


