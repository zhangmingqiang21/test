#写100以内的质数之和,冒泡排序，选择排序,去重
class A(object):
    def zhishu(self,x):
        c = 0
        for a in range(2,x):
            for b in range(2,a):
                if a % b == 0:
                    break
            else:
                c = c + a
                print(a)
        print(c)




    # def maopao(self):
    #     a="1,3,5,7,2,4,6"
    #     b=a.split(",")
    #     c = len(b)
    #     for x in range(c):
    #         for y in range(c-1):
    #             if int(b[y]) > int(b[y+1]):
    #                 b[y],b[y+1] = b[y+1],b[y]
    #     print(b)


#     def xuanze(self):
#         a = "99,1,3,5,7,2,4,23,21,12,56,46"
#         b = a.split(",")
#         c = len(b)
#         for x in range(c):
#             for y in range(x+1,c):
#                 if int(b[x]) > int(b[y]):
#                     b[x],b[y] = b[y],b[x]
#         print(b)

#
#     def shuzi(self):
#         b = 0
#         a ="13532"
#         while True:
#             b = b +1
#             if str(b) == a:
#                 print(b)
#                 break
#
#     def quchong(self):
#         a = [1,1,2,2,3,4,5,6,4,5]
#         b=[]
#         for i in a:
#             if i not in b:
#                 b.append(i)
#         print(b)
#     def jiujiu(self):
#         for i in range(1,10):
#             for j in range(1,i+1):
#
#             print(f"{i}*{j}={i*j}\t",end="")
#         print()

#
# aa=A()
# aa.zhishu(100)
# aa.maopao()
# aa.xuanze()
# aa.shuzi()
# aa.quchong()





#九九乘法表
for i in range(1,10):
    for j in range(1,i+1):

        print(f"{i}*{j}={i*j}\t",end="")
    print()

#python操作数据库
# import pymysql
# class A(object):
#     #连接数据库
#     def __init__(self):
#             self.connect=pymysql.connect(
#             host="192.168.10.199",
#             port=3306,
#             user="root",
#             password="111111",
#             charset="utf8"
#             )
#         #创建数据库
#     def create_database(self):
#         cur=self.connect.cursor()
#         sq1 = 'create database py11'
#         cur.execute(sq1)
#
#     #创建表格
#     def create_table(self):
#         cur = self.connect.cursor()
#         sq1 = 'use py11'
#         sq2 = 'create table sdf(name char(30),age int(10))'
#         cur.execute(sq1)
#         cur.execute(sq2)
#
#     #给表格添加数据
#     def insert(self):
#         cur=self.connect.cursor()
#         sq1 = 'use py11'
#         sq2 = 'insert into sdf values("zhang",21),("wang",22),("zhao",19)'
#         cur.execute(sq1)
#         cur.execute(sq2)
#
#     #查找数据库里表格的数据
#     def select(self):
#         cur = self.connect.cursor()
#         sq1 = 'use py11'
#         sq2 = 'select * from sdf'
#         cur.execute(sq1)
#         cur.execute(sq2)
#         a = cur.fetchall()
#         print(a)
# aa=A()
# # aa.create_database()
# # aa.create_table()
# aa.insert()
# aa.select()


# #使用python操作Excal表格
# import xlrd
# #打开博文1.xls这个表格
# d = xlrd.open_Workbook(filename="博文1.xls")
# #利用索引取第一个表格
# table1 = d.sheets()[0]
# #取第一行的所有数据
# x = table1.row_values(1,1)
# #取第一列数据
# # y=

a = [1,2,3,1,2,3,3,4,5,6]
print(set(a))

