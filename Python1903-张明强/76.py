import pymysql
class  A(object):
    def __init__(self):
        self.connect=pymysql.connect(
            host="192.168.10.199",
            port=3306,
            user="root",
            password="111111",
            charset="utf8",
            # database="zmq"
        )
    def create_database(self,aa):
        self.aa=aa
        cur=self.connect.cursor()
        sq1 = f"create database  {aa}"
        cur.execute(sq1)
    def create_table(self,bb,cc):
        cur = self.connect.cursor()
        sq1 = f"use {bb}"
        sq2 = f"create table {cc}(name char(20),age int(10))"
        cur.execute(sq1)
        cur.execute(sq2)
    def insert(self,dd,ee,ff,gg):
        cur = self.connect.cursor()
        sq1 = f"use {dd}"
        sq2 = f"insert into {ee} values({ff,gg})"
        cur.execute(sq1)
        cur.execute(sq2)


    def down(self):
        self.connect.close()
zmq=A()
# zmq.create_database("qwas")
# zmq.create_table("qwas","opkl")
zmq.insert("qwas","opkl","zhang","21")
