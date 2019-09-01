# while True:
# #     a = input("输入54188退出系统，输入任意键开始购买:")
# #     if a == "54188":
# #       break
# #     spm = ["喜羊羊","懒羊羊","沸羊羊","美羊羊","灰太狼","红太狼","暖羊羊","小灰灰"]
# #     dj = [75,60,40,60,70,30,50,80]
# #     kcl = ["999","888","777","666","555","444","333","222"]
# #     print("编号", "\t", "\t", "商品", "\t", "\t", "\t", "\t", "\t","价格", "\t", "\t", "\t", "库存", "\t", "\t", "\t")
# #     for e, f in enumerate(spm):
# #         print(e, "\t", "\t", "\t", f, "\t", "\t", "\t", "\t", dj[e], "\t", "\t", "\t", kcl[e], "\t", "\t", "\t")
# #     b = int(input("输入商品编号:"))
# #     c = int(input("输入购买数量:"))
# #     j = c * dj[b]   #非会员购买的的价钱
# #     # print(j)
# #     h = input("会员请输入卡号,非会员输入2:")
# #     if h == "2":    #如果输入2，直接显示总价j
# #         print(f"消费金额{j}元")
#     elif h == "666":   #如果输入1，进入会员系统
#         while   True:
#            i = int("10000")   #会员账户余额
#            print(f"会员卡总金额为{i}元")   #显示余额
#            k = j * 0.5     #会员打5折
#            if i < k:       #如果余额小于购买的总价，显示余额不足
#               print("余额不足")
#               break
#            else:
#                l = i - k    #使用会员卡消费的金额
#                m = i - k     #会员卡上所剩余额
#                print(f"消费金额{k}元")
#                print(f"会员卡剩余金额{m}元")
#                break
#









# print(sum(range(101)))

# def a(x):   #求和的代码，a是函数名，x是变量，变量为数字
#     i = 0
#     for b in range(x):
#         i = i + b
#     # print(a)
#     return     #把结果赋值给了函数a
# print(a((900)))



# a = "全局变量"
# print(a)

# def a():
#     b = "局部变量"
#     return b
# a()    #等价于"局部变量"
# print(a())


# 将局部变量转换为全局变量
# def zmq():
#     global c
#     print(c)
#     c = 100   #局部变量
#
# print(changed local c to: c)

# def a(x,y):
#     c = x + y
#     print(c)
#     return c
#            #在reuturn后面写东西不执行
#
#
#
# a(10,20)



 #用函数写阶乘之和
# def a(i):
#     a = 0
#     for x in range(1,i+1):
#         z = 1
#         for y in range(1,x+1):
#             z = z * y
#         a = a + z
#     return a
#
# print(a(5))


#
# def a(x,y=10):  #默认参数y=100
#     c = x + y
#     print(c)
#     return c
#            #在reuturn后面写东西     不执行
#
# a(10,100)    #，如果不写，默认10+10，如果y的参数写了，那么就使用写的那个参数


# def a(*args):
#     x,y,z = args
#     print(x)
#     print(y)
#     print(z)
#
# a(1,2,3)



# def a(*args):
#     n = 0
#     for i in args:
#         n = n+ 1
#         print(f"参数是x_{n},对应值{i}")
#
# a(1,2,"hh")

# def a():
#     global p   #p代表全局变量
#     p = 12
#
# a()
# print(p)  #验证p是否为全局变量


# )g = "全局变量"   #str
# def a():
#     global g
#     g = 100
#     print(g)
# a(

# def a(**kwargs):
#     print(kwargs)   #关于字典的所有函数都可以使用
#
#
# #传统写法一
# # a(x=1,y=2,z=3)
#
# #写法二
# x = {"1":12,"2":23,"3":34,"4":45}    #先写一个字典
# a(**x)


#冒泡排序
# def a(*args):
#     x = list(args)   #先转换位列表
#     for w in range(len(x)):    #数字有几个 ，大循环就循环几次
#         for y in range(len(x)-1):   #小循环，只能循环到倒数第二个，如果不减一，最后一个索引值无法和下一个比较，超出索引范围
#             if int(x[y]) > int(x[y+1]):   #如果前一个比后一个大，
#                 x[y],x[y+1] = x[y+1],x[y]   #那么就将就两个值换位子
#     print(x)
#     # return x
# a(1,2,3,4,7,6)


# def a():
#
#     b = input("输入账号:")
#     c = input("输入密码:")
#     x = b.split(",")
#     y = c.split(",")
#     i = []
#     j = []
#
#     for m in range(len(x)):
#         if len(x) != len(y):
#             print("输入错误")
#             break
#         elif  5 <= len(x[m]) <= 8 and 6 <=len(y[m]) <=9:
#             i.append(x[m])
#
#             j.append(y[m])
#     return(f"账号:{i},密码:{j}")
#           # else:
#           #    print(f"输入错误")
# print(a())



# def a():      #嵌套函数
#     return  "a返回的"
# def b():
#     print("此时运行函数b")
#     print(a())
# b()



# def foo():
#     x = 100  #局部变量
#
#     def k():
#         c = x * 10
#         return c
#     return k()
#
# # foo()
# print(foo())


# li=[{"age":20,"name":"def"},{"age":25,"name":"abc"},{"age":10,"name":"ghi"}]
# li=sorted(li, key=lambda x:x["age"])
# print(li)



# class Students(object):   #定义一个类
#     # height = 170
#     # weight = 55
#     def zmq(self,x,y,z):
#          print(f"他的名字是{x}，他的身高是{y}cm,他的体重是{z}kg")
#
# #类的使用
# s1=Students()   #被称为对象，类的实例
# s1.zmq("博文",180,55)        #类的实例，使用类的方法


#
# class ab(object):
#     x = "林耀东"
#     y = "男"
#     z = "1967-5-20"
#     m = "广东"
#     n = "塔寨"
#     i = "制毒、贩毒"
#     j = "村主任"
#
#
#     def b(self):
#         print(f"名字:{self.x},性别:{self.y},出生日期:{self.z},出生地:{self.m},居住地:{self.n},专业:{self.i},职位:{self.j}")
# c= ab()
# c.b()




#如果用_init_方法在类名括号里面吧参数写进去
# class A(object):  #类的属性，
#      banji = "三班"
#       # __sex = "男"   #私有属性
#      def __init__(self,name,age):   #如果定义了init方法，在创造对象的时候，必须传入参数
#            #对象的属性
#          self.name = name
#          self.age = age
#      def show(self):  #类的普通方法
#          # 局部变量
#
#          print(f"名字:{self.name},年龄:{self.age}，班级:{self.banji}")
#      @staticmethod
#      def doo():    #静态方法-->类似于函数
#       print("类的静态方法")
#      @classmethod
#      def koo(cls):     # 类方法，cls和self的作用一致，只是换个名字而已
#          print("类的类方法")
#      def __too(self):
#           print("类的私有方法")
#      def ok(self):
#          self.__too()  #支持所有的方法名
#
# c = A("博文",12)   #创造对象的过程
# c.show()     #对象使用类的方法，类的方法，只有类的对象才能使用
# c.doo()
# c.koo()
# c.ok()




#继承
# class B(object):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def say(self):
#         print(f"B类中的普通方法")
#         return self.name,self.age
#
# #英文的括号()  继承于括号内的类   ，只要被继承类有的，继承类都可以使用
# class C(B):
#     def talk(self):
#         res = super().say()    #输入super向上找方法
#         print(res)
#
#         #多态   重写方法
#     def say(self):
#         print("C类里的方法")
#
# C1 = C("张三",56)
# C1.talk()




#多态：继承类对被继承的方法的重写{方法名一样，语句块不一样}
#如何在多态之后使用被继承类的方法：使用  super().被继承的方法



# for m in range(1,10):
#
#     for n in range(1,10):
#
#         if m>=n:
#
#             print('%s×%s=%s'%(m,n,m*n),end=' ')
#
#     print()



#把九九乘法表写入Excal表格
# import xlwt
# d = xlwt.Workbook()
# table = d.add_sheet("九九乘法表")
#
# for i in range(1, 10):
#     for j in range(1, i+1):
#         # print('{}x{}={}\t'.format(j, i, i*j), end='')
#     # print()
#         table.write(i-1,j-1,f"{j}*{i}={i*j}")
# d.save("博文323.xls")


#吧九九乘法表写入txt文件





#爬虫  使用到的库  requests    有目的的获取网络中的资源
# import re
# import requests

# d ={"User_Agent" :"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",}


#发送url请求
# req = requests.get('https://www.fpzw.com/xiaoshuo/88/88413/17355844.html',headers=d)
#接收html文本
# res = req.content.decode('gbk')
# print(res)
# s1 = re.compile('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)</p></div>')
# s2 = re.compile('<h2>(.*?)</h2>')
# s3 = re.compile('<dd><a href="(.*?).html">(.*?)</a></dd>')
# a=re.findall(s1,res)
# b= re.findall(s2,res)
# c = re.findall(s3,res)
# print(c)
# print(b)
# print(a)
# s1= re.compile('<title>\s*(.*)\s*</title>')
# a = re.findall(s1,res)
# print(a)



#os.path 类,   对文件的操作
# #1.返回文件的绝对路径  ：os.path.abspath('文件名')
# a=os.path.abspath('aa.py')
# print(a)
# #2.返回文件上一级目录
# b=os.path.dirname(r'D:\PyCharm 2019.1.3\xiangmu\B')
# print(b)
# #3.返回文件的文件名
# c=os.path.basename(r'D:\PyCharm 2019.1.3\xiangmu\B\bb.py')
# print(c)
# #4.判断文件是否存在，  返回布尔值
# d=os.path.exists(r'D:\PyCharm 2019.1.3\xiangmu\B\bb.py')
# print(d)
# #5.判断是否为目录
# e=os.path.isdir('B')
# print(e)
# #6.判断是否为文件
# f=os.path.isfile('bb.py')
# print(f)
# #7.判断是否为链接文件
# g=os.path.islink('bb.py')
# print(g)
# #8.文件路径拼接
# h=os.path.join('/user/','abc')
# print(h)
# #9.文件路径分离，将前一个文件/目录  于最后一个进行分割，返回一个元祖
# i=os.path.split(r'D:\PyCharm 2019.1.3\xiangmu\B\bb.py')
# print(i)
# #10.分割文件的后缀名，返回一个元祖
# j=os.path.splitext(r'D:\PyCharm 2019.1.3\xiangmu\B\bb.py')
# print(j)


# python与系统的交互
# 系统包括：window   mac  unix
# python的内置模块：   python自带的，下载是包含的
# OS库

# # 导入OS模块
# import  os
# # 获取当前所在的位置  ： os.getcwd()
# a=os.getcwd()
# print(a)
# #切换到指定目录 ：os.chdir(目录的名字）
# os.chdir('B')
# b=os.getcwd()
# print(b)
# #当前目录：os.curdir
# #s上一级目录：os.pardir
# os.chdir(os.pardir)
# c=os.getcwd()
# print(c)
#
# #获取操作系统类型  os.name      nt:window
# n=os.name
# print(n)
# #创建多级目录  os.makedirs('a/b/c')
# #创建一个目录：os.mkdir('a')
# #删除多个空目录：os.removedirs('a')
# #删除单个空目录 ：os.rmdir('a')
# #查看当前路径下所有的文件，目录，包括隐藏的 :os.listdir('绝对路径')
# k=os.listdir(r'D:\PyCharm 2019.1.3\xiangmu\B')
# print(k)

#对文件，目录进行重命名： os.rename('路径/文件名,'路径/新文件名')
#删除文件：os.remove('路径/文件名')
#执行系统命令
# kk=os.popen('dir')
# print(kk.read())
#目录树： os.walk('路径/目录’)


# import os
# a = os.getcwd()
# # print(a)
# b=os.curdir
# # print(b)
# c=os.pardir
# # print(c)
# d=os.name
# # print(d)
# a1=os.removedirs("A/B/C/D/E/F/G/H/I/J/K/L/M")
# # print(a1)
# a2=os.mkdir("A/a.txt")
# print(a2)


#查看当前目录下的目录文件、普通文件、连接文件的个数
# import os
# a=os.listdir(r"C:\Users\86157\Desktop\Python1903-张明强")
# x=0
# y=0
# z=0
# for i in  a:
#     if  os.path.isdir(i):
#         x=x+1
#     elif os.path.isfile(i):
#         y = y+1
#     elif os.path.islink(i):
#         z=z+1
# print(f"目录文件的个数:{x}")
# print(f"普通文件的个数:{y}")
# print(f"链接文件的个数:{z}")

#因数之和等于本身的
for i in range(1,101):
    b=0
    for  j in range(1,i):
        if i%j == 0:
            b=b+j
    if b==i:
        print(i)













