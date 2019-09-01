# class A(object):
#     def zmq(self,x,y,z):    #三个必填函数
#          c = x + y + z
#          return c
#
# class B(A):
#     def ok(self,s,x,y,z):
#         q=self.zmq(x,y,z)
#         w = s +q
#         print(w)
# # b = A()
# # print(b.zmq(1,2,3))  #使用A类里面的zmq这个函数
# c=B()
# c.ok(1,2,3,3)

#连接数据库
import pymysql   #导入pymysql这个包
class A(object):
    def __init__(self):
            self.connect=pymysql.connect(            #连接
                host = "192.168.10.21",
                port = 3306,
                user = "root",
                password = "111111",
                charset = "utf8")
#创建数据库
    def create_database(self):
        cur = self.connect.cursor()
        sq1 = "create database python31"
#         cur.execute(sq1)
# dc = A("123")
# dc.create_database()

#创建表格

    def create_table(self):
        cur = self.connect.cursor()
        sq1 =  "use python31"
        sq2 = "create table df (name char(20),age int(10))"
#         cur.execute(sq1)
#         cur.execute(sq2)
# sx = A()
# sx.create_table()

#给表格添加数据
    def jia(self):
        cur = self.connect.cursor()
        sq1 = "use python31"
        sq2 = "insert into df values   "
        cur.execute(sq1)
        cur.execute(sq2)
az = A()
az.jia()

