# import xlwt     #导入xlwt
# sheng=['北京市','天津市','河北省','山西省','内蒙古自治区','辽宁省',
#           '吉林省','黑龙江省','上海市','江苏省','浙江省','安徽省','福建省','河南省','广东省','云南省']
#
# pro=['各省市','工资性收入']
#
# money=['5047','3247','1514','1374','590','1499','605','654','6686','3104','3575','1184','1855','1441','1671','1022']
#
# d = xlwt.Workbook()   #新建一个excal文件
# table = d.add_sheet("工资表")   #设置表名
# #第一次for循环将两个表头插入
# j = 0
# for i in pro:
#     table.write(0,j,i)   #行不变，列变
#
#     j = j + 1
# #第二次循环将所有省份插入到
# m = 1
# for k in sheng:
#
#     table.write(m,0,k)   #行变列不变
#     m = m + 1
#
# l = 1
# for g in money:
#     table.write(l,1,g)
#     l = l +1
# d.save("博文211.xls")


# class A(object):
#     def aa(self):
#         for a in range(101):
#              for b in range(2,a+1):
#                   if a % b == 0:
#                       break
#              if a == 2:
#                     return a
# q = A()
# q.aa()
#

#统计当前目录下有多少文件
# import os
# class  A(object):
#     # s=r'C:\Users\86157\Desktop\Python1903 - 张明强'
#     def hehe(self,x):
#         x=os.listdir(x)   #查看目录下所有文件
#         a = 0
#         b = 0
#         for i in x:
#             if os.path.isfile(i):
#                 a = a + 1
#             elif os.path.isdir(i):
#                 b = b + 1
#         print(f'文件个数:{a}')
#         print(f'目录个数:{b}')
#         # return a
# B=A()
# B.hehe(os.getcwd())


#python对时间的操作
import time
#time
  #1睡眠
# print("hehe")
# time.sleep(5)  #cpu进程休息5秒
# print("haha")

  #2.cpu运算一串代码所需要的时间
# print(time.clock())   #从第一行运行到所在行花费的时间

#3.本地时间
# print(time.ctime())


#4.本地时间
# print(time.asctime())

#5.输出详细的时间信息
# print(time.localtime())

#6格式化输出时间
# print(time.strftime("%A %d %B %H:%M:%S" ))


#根据格式解析表示时间的字符串
# print(time.strptime("30 Nov 00 ","%d %b %y"))


#距离计算机元年过去的秒的总和
# print(time.time())



#python对日期的操作
#datetime
# import datetime
from datetime import datetime,timedelta,date
#1获取当前时间/日期
# print(datetime.now())


#2获取指定的时间日期
# print(datetime(1996, 5, 20, 13,14,00))

#3字符串转日期
# t = datetime.strptime('1996-05-20 13:14:00','%Y %m %d %H:%M:%S')
# print(t)


#4
# a = datetime.now().strftime("%A %d %B %H:%M:%S")
# print(a)


#5 datetime加减
# now = datetime.now()
# z = now - timedelta(days=199999)
# print(z)


# 6获取当前日期
# print(date.today())

#7日期的加减
f = date.today() - timedelta(days=2)
print(f)
