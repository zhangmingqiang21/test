# 读取这个表格
# import xlrd
#打开这个表格
# d=xlrd.open_workbook(filename="as1.xls")

#选择第一个表格
# table=d.sheets()[0]

#查看第一行数据
# row=table.row_values(0)
# print(row)

#查看第一列数据
# col=table.col_values(0)
# print(col)

#查看列数
# x=table.ncols
# print(x)

# 查看行数
# y=table.nrows
# print(y)

#查看整张表格,一列数据为一个大列表
# for i in range(x):
#     print(table.col_values(i))


# 查看整张表的数据
# for j in range(y):
#     print(table.row_values(j))

#向表格内插入数据
# import xlwt
# import xlrd
# d=xlwt.Workbook()
# f=xlrd.open_workbook(filename="as1.xls")
# # table=d.add_sheet("000")
# # table.write(0,0,"zhang")
# table=f.sheets()[0]
# row=table.nrows
# col=table.ncols
# for i in range(row):
#     for j in range(0,10):
#         table.write(i,0,j)
# d.save("qw.xls")


# import xlrd
# d=xlrd.open_workbook(filename="as1.xls")
# table=d.sheets()[0]
# row=table.row_values(0)
# col=table.col_values(0)
# x = table.nrows
# y = table.ncols
# for i in range(x):
#     print(table.row_values(i))
#
# for j in range(y):
#     print(table.col_values(j))

# import xlwt
# d=xlwt.Workbook()
# table=d.add_sheet("信息表1")
# d1=open(file="a.txt",mode="r",encoding="utf-8")
# a=d1.read()
# b=a.split("\n")
# c=[]
# for i in b:
#     i1=i.split("\t")
#     c.append(i1)
# # print(c)
# k=len(c)
# for j in range(k):
#     for j1 in range(len(c[j])):
#         table.write(j,j1,c[j][j1])
# d.save("11.xls")

#阶乘之和
# c=0
# b=1
# for a in range(1,6):
#     b=b*a
#     c=c+b
# print(c)

#质数之和
# c=0
# for a in range(2,100):
#     for b in range(2,a):
#         if a%b==0:
#             break
#     else:
#         c=c+a
# print(c)


# from selenium import webdriver
# from time import sleep

# driver = webdriver.Chrome()
#最大化窗口
# driver.maximize_window()
# driver.get('http://mail.163.com/')
# sleep(2)
#切换到表单
# driver.switch_to.frame("x-URS-iframe1565009089578.531")
# driver.find_element_by_name("email").clear()
# driver.find_element_by_name("email").send_keys('JSDU0820@163.com')
# driver.find_element_by_name("password").clear()
# driver.find_element_by_name("password").send_keys('zhang967700zmq')
# driver.find_element_by_id("dologin").click()
import pytest
import allure_pytest
