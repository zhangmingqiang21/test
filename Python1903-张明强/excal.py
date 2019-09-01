#题目：判断输入的三个数大小关系
# a = int(input("请输入第一个数字:"))
# b = int(input("请输入第二个数字:"))
# c = int(input("请输入第三个数字:"))
# if a - b > 0 and b - c > 0:
#     print(a,b,c)
#
# elif  a - b < 0 and b - c < 0:
#     print(c,b,a)
#
# elif a - b == 0 and b - c == 0 and a - c ==0:
#     print("相等你不知道？")
# elif  b - a > 0 and  a - c > 0:
#     print(b,a,c)
#
# elif  a - c > 0 and c - b > 0:
#     print(a,c,b)
#
# elif b - c > 0 and  c - a  > 0:
#     print(b,c,a)
#
# elif c - a > 0 and a - b > 0:


#题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# x = 0
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if( i != k ) and (i != j) and (j != k):
#               # print (i,j,k)
#               x = x +1
# print(x)
              # c  =  print(i,j,k)


#题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%
      #提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成
      #3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？



#题目： 一张纸0.08mm 需要折多少次能超过珠穆朗玛峰（8848m）8848000mm
# a = 8848000
# b = 0.08
# c = 0
# while True:
#     c = c +1  #c=0时，开始进行第一次折叠，  当进行第二次折叠
#     b = b * 2  #这时这张纸的厚度为0.08*2=0.16，这时纸的厚度为0.16*2=0.32
#     if b > a:    #以此类推，当b大于a的时候，显示结果
#      print(c)
#      break  #终止循环

#题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
# for i in range(1,85):
#     if 168 % i == 0:
#         j = 168/i
#         if i > j and (i + j)%2 ==0 and (i - j)%2 ==0:
#            m = (i + j)/2
#            n = (i - j)/2
#            x = n * n -100
#            print(x)


#题目：输入三个整数x,y,z，请把这三个数由小到大输出。
# x = int(input("输入第一个数:"))
# y = int(input("输入第二个数:"))
# z = int(input("输入第三个数:"))
# if x - y >0 and y -z >0:
#     print(z,y,x)
# elif x - z >0  and  z - y >0:
#     print(y,z,x)
# elif y - z > 0 and z -x > 0:
#     print(x,z,y)
# elif y -x > 0 and x -z > 0:
#     print(z,x,y)
# elif z - x > 0 and x -y >0:
#     print(y,x,z)
# elif z - y > 0 and y - x >0:
#     print(x,y,z)


# l = []
# for i in range(3):
#     x = int(input('输入数字:\n'))
#     l.append(x)
# l.sort()
# print (l[::-1])
# # print(l)

# a= "hello"
# b = "22"
# print(a.join(b))

C:\Users\86157\Desktop\Python1903-张明强\excal.py
import xlrd
import xlwt
# #打开excal文件
d = xlrd.open_workbook(filename="博文6.xls")
# #获取excal表
table  = d.sheets()[0]   #使用索引获取第一个表格
x = table.row_values(1,1)    #使用索引获取第一行的数据
y = table.row(1)[1].value   #利用索引  显示一行,返回一个列表，想要获取某一个元素，需要利用索引值，使用value拿到具体的值
print(y)   #返回的结果是包含所有excal的列表
# z = table.col(0)[1]
# i = table.cell(1,1).value    #类似于坐标取值
# j = table.ncols   #获取列数
# k = table.nrows

#取出每行的数据
# for g in range(k):
#     print(table.row_values(g) )

#取出每列的数据
# for f in range(j):
#     print(table.col_values(f))

#打印输出Excal表格的名字,
# print(d.sheet_names())   #打印所有Excal表格的名字

# n = d.sheet_by_index(1)   #返回在内存中的位置
# print(n)
# print(z)
# print(i)
# print(j)
# print(k)

# class Excal(object):
#     def __init__(self):
#         self.d = xlrd.open_workbook(filename="zmq.xlsx")  #打开这个表格
#         self.t = self.d.sheet_by_index(0)      #找到这个表格
#
#     #data方法获取一张表作用数据
#     def  data(self):
#         #将所有数据装到一个列表
#         s = []
#         n = self.t.nrows
#         for i in range(n):
#             print(self.t.row_values(i))
#             s.append(self.t.row_values(i))
#         return s
#
# class Txt(Excal):
#     def write_data(self):
#         f = open(file="a.txt",mode="w",encoding="utf-8")
#         shuju = self.data()
#         for i in shuju:
#             for j in i:
#                 f.write(f"{str(j)}\t")
#             f.write("\n")


# ok = Excal()
# ok.data()





# t1 = Txt()




























