#python与系统的交互
#系统包括：windows，mac。unix
#python的内置模块-->python自带的，下载时包含的
#os库
import os
#获取当前目录
# a = os.getcwd()
# print(a)
# #切换目录
# b=os.chdir('A')
# print(b)
#
# #当前目录
# c=os.curdir('.')
# print(c)
#
# #上一级目录
# os.chdir(os.pardir)
# d = os.getcwd()
# print(d)

#获取系统操作类型
# n = os.name
# print(n)   #nt是Linux


#创建多级目录
# os.makedirs('AAA/BBB/CCC')

#创建一个目录
# os.makedir('jhfhA')



#删除多个目录,只能删除空目录
# os.removedirs('AAA/BBB/CCC')

#删除单个目录,只能删除空目录
# os.remdir()

#查看当前路径下的所有文件，目录，包括隐藏文件
# x= os.listdir(r'C:\Users\86157\Desktop\Python1903-张明强')
# print(x)   #返回的是一个列表


#对文件或者目录重命名
# os.rename(r'C:\Users\86157\Desktop\Python1903-张明强\博文111.xls',r'C:\Users\86157\Desktop\Python1903-张明强\博文444.xls')   #吧博文111.xls更改为博文444.xls

#执行本机系统命令
# a=os.popen('dir')
# print(a.read())


#目录树
#os.walk 类似于tree
for i,j,k in os.walk(r'C:\Users\86157\Desktop\Python1903-张明强'):
    print(k)
