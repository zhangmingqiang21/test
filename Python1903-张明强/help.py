"""
import pymysql   #导入mysql这个包
connect = pymysql.connect(
    host = "192.168.10.43" ,   #数据库所在的主机IP地址/域名【云服务器--mysql数据库】
    port = 3306,    #mysql的端口号
    user = "root",    #mysql的用户名
    password = "111111",    #mysql的密码
    charset = "utf8",     #mysql的编码方式
    database = "zmq" ,    #数据库名,不写的话，默认所有库
)

cur = connect.cursor()    #游标 ，类似于mysql的命令行模式
sql = "create database python2"   #创建一个库
# sql1 = "drop database python2"   #删除一个库

cur.execute(sql)   #实行这个命令
print(cur)
"""

#面向对象
import pymysql

class A(object):

    #连接mysql数据库
    def __init__(self):
        self.connect= pymysql.connect(
            host="192.168.10.21",
            port=3306,
            user="root",
            password="111111",
            charset="utf8",
        )
        #创建库
    def create_database(self):
        cur = self.connect.cursor()  # 游标
        sql = "create database python11"  # 创建python4这个库


        cur.execute(sql)  # 实行这个命令
dc = A()
dc.create_database()
#
#      #创建表格
#     def create_table(self):
#         cur = self.connect.cursor()  # 游标
#         sq1 = "use python5"  # 进入python1 这个库
#         sq2 ="create table timu(name char(20),sex char(10),age int(20),hight varchar(20),country varchar(20))"
#         cur.execute(sq1)    # 实行进入python1这个数据库的命令
#         cur.execute(sq2)  # 实行这个创建sql语句
#
#     #给表格添加数据
#     def insert(self,qwe):
#         cur = self.connect.cursor()
#         sq1 = "use python5"
#         sq2 = f'insert into timu values  {qwe}'
#         cur.execute(sq1)    #实行进入python1这个数据库的命令
#         cur.execute(sq2)   #实行添加数据的这个命令
#

#     def find(self):
#         cur = self.connect.cursor()
#         sq1 = "use python5"
#
#         sq2 = "select * from timu"    #执行查询 timu这个表
#         sq = cur.execute(sq1)       #执行sq1语句
#         a = cur.execute(sq2)       #执行sq2语句
#         b  = cur.fetchall()     #查询sql语句获得所有结果
#         # print(sq2)
#         print(b)
#
#
#
# #与数据库断开连接
#     # def close(self):

#     #     self.connect.close()



# my = A()
# # my.create_database()
# # my.create_table()
# # my.insert()
# my.find()
#
#
# my.find()
# # my.create_table()
# d = {
#     "data": {
#         "msg":
#         [
#             {
#                 "s_1": ["Jim", "男",  19, "175"
#                                          ""
#                                          ""
#                                          "cm"],
#                 "country": "美国"
#             },
#             {
#                 "s_2": ["Kity", "女",  17, "165cm"],
#                 "country": "法国"
#             },
#             {
#                 "s_3": ["Tom", "男",  19, "173c"
#                                          ""
#                                          ""
#                                          ""
#                                          "m"],
#                 "country": "美国"
#             },
#             {
#                 "s_4": ["拖拉斯基", "男",  18, "180cm"],
#                 "country": "俄罗斯"
#             },
#             {
#                 "s_5": ["阿卡丽", "女",  17, "175cm"],
#                 "country": "乌克兰"
#             },
#             {
#                 "s_6": ["牙买稻子", "女",  18, "161cm"],
#                 "country": "日本"
#             },
#             {
#                 "s_7": ["龟田一郎", "男",  19, "175cm"],
#                 "country": "日本"
#             },
#             {
#                 "s_8": ["张三", "男",  20, "180cm"],
#                 "country": "中国"
#             },
#             {
#                 "s_9": ["李秀琴", "女",  19, "175cm"],
#                 "country": "中国"
#             },
#             {
#                 "s_10": ["宋仲基", "女",  19, "175cm"],
#                 "country": "韩国"
#             },
#             {
#                 "s_11": ["金正鞋", "男",  19, "168cm"],
#                 "country": "朝鲜"
#             },
#             {
#
#
#
#
#
#
#
#
#                 "s_12": ["卡列夫斯基", "男",  21, "190cm"],
#
#
#
#                 "country": "俄罗斯"
#             },
#         ]
#     },
# }
#
#
# # self.connect.commit        # 保存数据到数据库
# x = d["data"]   #取出字典d里面data键的值
# y = x["msg"]     #取出data字典里面msg的列表
# n = 0
# for i in y:
#     n = n +1
#     j = i[f"s_{n}"]   #显示每个列表
#     m = i["country"]       #取每个列表的最后一位
#     j.append(m)
#     p= tuple(j)
#     my.insert(p)


# import xlwt
# d = xlwt.Workbook()   #新建一个excal文件
# table = d.add_sheet("表一")    #新建一个excal表，表名必填
# table.write(0,0,"张三")   #写入数据到表格，一次写入一个单元格
# d.save("71.xls")   #保存表格，括号内为表名，必填

# import  xlwt
# a = [
#     ["学号","姓名","年龄","性别"],
#     [1,"张三",12,"男"],
#     [2,"李四",13,"女"],
#     [3,"王五",14,"男"],
#     [4,"赵六",15,"女"]
#     ]
# d = xlwt.Workbook()   #新建一个excal表格
# table =d.add_sheet(x)   #设置表名
# row = 0
# for i  in  a:    #i就是每个小列表
#     col = 0
#     for j in i:
#
#         table.write(row,col,j)
#         col = col + 1
#     row = row + 1
# d.save("博文3.xls")



# import  xlwt
# class A(object):
#     AA = "x"   #类的属性
#     def __init__(self,x):
#         self.x= x   #方法的属性
#         self.d = xlwt.Workbook()  # 新建一个excal表格
#         self.table = self.d.add_sheet(x)     #设置表名为x这个变量
# class ok(A):
#     def talk(self,x):
#         A.__init__(self,x)
#         self.x = x
#         row = 0
#         for i in a:  # i就是每个小列表
#             col = 0
#             for j in i:
#                 self.table.write(row, col, j)
#                 col = col + 1
#             row = row + 1
#         self.d.save(self.x)
# ji = A("博文11.xls")
# ji.talk()



























