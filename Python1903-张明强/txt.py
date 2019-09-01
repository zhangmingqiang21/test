# import xlwt
# d=xlwt.Workbook()
# table=d.add_sheet("sheet1")
# d1=open(file="a.txt",mode="r",encoding="utf-8")


# for i in range(1,100):
# x=d1.read()
# for i in range(0,10):
#     # for j in range(0,10):
#     table.write(i,0,x)
# d.save("aaa.xls")



# import xlwt
# d=xlwt.Workbook()
# table=d.add_sheet("表1")
# d1=open(file="a.txt",mode="r",encoding="utf-8")
# x=d1.read()
# print(x)
# x1=x.split("\n")
# # print(x1)
# z=[]
# for i in x1:
#     x3=i.split("\t")
#     z.append(x3)
# # print(z)
# g=len(z)
# for m in range(g):
#     for n in range(len(z[m])):
#         table.write(m,n,z[m][n])   #取出每个列表里面的小元素
# d.save("as1.xls")

# for a in range(0,100):
#     for b in range(0,100):
#         for c in range(0,100):
#             if a+b+c==100 and 2*a+b+0.*c==100:
#                 print(f"公鸡个数:{a},母鸡个数:{b},小鸡个数:{c}")



# a=0
# for i in range(2,100):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         a=a+i
# print(a)

# for i in range(1,100):
#     k=0
#     for j in range(1,i):
#         if i%j==0:
#             k=k+j
#     if i==k:
#         print(i)

# 读取excal表格的命令
# import xlrd
# d=xlrd.open_workbook()
# table=d.sheets()[0]
# row=table.row_values()
# col=table.col_values()
# x=table.nrows
# y=table.ncols
# for i in range(x):
#     print(table.row_values(i))
# for j in range(y):
#     print(table.col_values(j))

# 写入excal表格的操作
# import xlwt
# d=xlwt.Workbook()
# table=d.add_sheet("biaoming")
# table.write(0,0,"asd")


# 读取txt文件的操作
# d=open(file="a.txt",mode="r",encoding="utf-8")
# d.read()

# 写入txt文件的操作
# d=open(file="b.txt",mode="w",encoding="utf-8")
# d.write("zhang")

# import os
# a=os.getcwd()
# b=os.listdir(a)
# x=0
# y=0
# z=0
# for i in b:
#     if os.path.isfile(i):
#         x=x+1
#     elif os.path.islink(i):
#         y=y+1
#     elif os.path.isdir(i):
#         z=z+1
# print(x)
# print(y)
# print(z)

import re,requests
class tp(object):
    def pres(self):
        url='http://image.baidu.com/search/detail?ct=503316480&z=0&ipn=false&word=%E5%A4%B4%E5%83%8F%E7%94%B7&step_word=&hs=0&pn=0&spn=0&di=199650&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=0&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=-1&cs=2324155658%2C1001151650&os=1038379538%2C3041393610&simid=4166282418%2C755300732&adpicid=0&lpn=0&ln=3272&fr=&fmq=1563796686617_R&fm=rs6&ic=undefined&s=undefined&hd=undefined&latest=undefined&copyright=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=head&bdtype=0&oriquery=%E5%A4%B4%E5%83%8F&objurl=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fblog%2F201512%2F25%2F20151225000843_uF3tX.thumb.700_0.jpeg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3B17tpwg2_z%26e3Bv54AzdH3Fks52AzdH3F%3Ft1%3Dcadmc9nc9&gsm=0&rpstart=0&rpnum=0&islist=&querylist=&force=undefined'
        head={'user_Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Mobile Safari/537.36'}
        res=requests.get(url=url,headers=head)
        html=res.content.decode('utf-8')
        return html
    def pres1(self):

        s=re.compile('li class="imgitem" title="(.*?)data-idx="(.*?)"><div class ="img-box"><img src="http://(.*?)" width="(.*?)" height="(.*?)"></div></li> ')
        s1=s.findall(self.pres())
        # print(s1)
        return s1
    def save(self):
        for i in self.pres1():
            res=requests.get(i[1])
            h1=res.content
            with open(f"{i[0]}.jpg","wb") as f:
                f.write(r"http://img5.imgtn.bdimg.com/it/u=1109507497,1637582812&fm=26&gp=0.jpg")
# a=tp()
# a.pres()
# a.pres1()
# a.save()
with open(f"123.jpg", "wb") as f:
    f.write("http://img5.imgtn.bdimg.com/it/u=1109507497,1637582812&fm=26&gp=0.jpg")









