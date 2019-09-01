# a = int(input("输入第一个数字:"))
# b = int(input("输入第二个数字:"))
# c = int(input("输入第三个数字:"))
# if a + b <= c or a + c <= b or b + c <=a:
#     print("不是三角形")
# elif a == b and b == c:
#     print("正三角形")
# elif a**2 + b**2 == c**2 or a**2 + c**2 ==b**2 or b**2 + c**2 == a**2:
#     print("直角三角形")
# elif a ==b or b ==c or a == c:
#     print("等腰三角形")
# elif a**2 + b**2 > c**2 or a**2 + c**2 >b**2 or b**2 + c**2 > a**2:
#     print("锐角三角形")
# elif a**2 + b**2 < c**2 or a**2 + c**2 >b**2 or b**2 + c**2 < a**2:
#     print("钝角三角形")


# a = { "x":["qwe","sad","zxc"],
#       "y":["bowen","python","1903"],
#       "z":["中国","河南","开封"],
#       }
# b = a.pop("x")
# seq = ["1","3","5"]
# new_a = dict.fromkeys(seq,"新乡")
# print(new_a)
# c = a.items()
# for  i,j in c:
#     print(i,j)

# a = {1:"hello","a":"字典一"}
# b = {2:"world","b":"字典二"}
# c = a.update(b)   #把b的元素放进a
# print(c)
# print(b)
# print(a)

# k = {1:12,2:13 }
# # k.setdefault("key1","hehe")
# # l = str(k)
# # print(l)

#去除列表中重复的元素
# a = [1,1,3,4,5,3,4,5]
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)

#去除列表中重复的元素
# a = [1,2,2,3,4,3,4,4,5,5]
# for b in a:
#     if a.count(b) > 1:
#         a.remove(b)
# print(a)

#输入的字符串变为字典键
# a = input("输入键")
# b = input("输入值")
# x = a.split(" ")
# y = b.split(" ")
# z = {}
# for i in range(0,len(x)):
#     if len(x) > len(y):
#         if x[i] > y[i]:
#             z.setdefault(x[i])
#         else:
#             z.setdefault(x[i],y[i])
#     else:
#          z.setdefault(x[i],y[i])
# print(z)

# s = {
#     "key1": [1000, 2000, 3000],
#     2019: ["hello",{"python": ['py2.x', 'py3.x']},],}

# # 求 key1 对应value的和
# v = s.get("key1")
# print(v)
# i = 0
# for j in v:
#     i = i + j
# print(i)

# 求 python 对应的值,并将每个版本的首字符大写、尾字符大写输出
# v = s.get(2019)  #取出2019这个键对应的值   ["hello",{"python": ['py2.x', 'py3.x']},],}
# n = v[1]         #利用索引值取出第二个数据    {"python": ['py2.x', 'py3.x']}
# m = n.get('python')    #取出python这个键对应的值     ['py2.x', 'py3.x']}
# x = m[0]         #取出'py2.x'
# y = m[1]          #取出'py3.x'
# z = x + y
# print(str(m).title())   #更改数据类型
# print(y.title())


# c = 0
# for a in range(2,101):
#     for b in range(2,a):
#         if a % b == 0:
#             break
#         else:
#             a = b
#             c = a + b
# # print(c)

# a= ()
# a = (1,2,5,{"100":[90,78,56]})
# b = ("sd","sd","sfs","sFfw")
# # c = a + b
# del b
# print(b)

# s = '[Description("衣物挑战5kg")]@        /medal/201906/24/Cloth_Single_5.png         @        /medal/201906/24/Cloth_Single_5_Get.png     @            [Description("衣物挑战10kg")]@        /medal/201906/24/Cloth_Single_10.png        @        /medal/201906/24/Cloth_Single_10_Get.png    @            [Description("衣物挑战15kg")]@        /medal/201906/24/Cloth_Single_15.png       @        /medal/201906/24/Cloth_Single_15_Get.png   @            [Description("衣物挑战20kg")]@        /medal/201906/24/Cloth_Single_20.png       @        /medal/201906/24/Cloth_Single_20_Get.png    @           [Description("衣物挑战25kg以上")]@        /medal/201906/24/Cloth_Single_25.png        @        /medal/201906/24/Cloth_Single_25_Get.png   @            [Description("衣物累计50kg")]@        /medal/201906/24/Cloth_Sum_50.png           @        /medal/201906/24/Cloth_Sum_50_Get.png'
# m = s.split()
# k = []
# p = []
# for i in m:
#     if i.find("Get") != -1:  #返回值不为-1，证明有
#         k.append(i)      #将i写入k这个列表
#     elif i.find("png") != -1:
#         p.append(i)
# print(k)
# print(p)
# for j in m:
#     if j.find("5.png") != -1:
#         p.append(j)
# print(p)



# a = {"1","python","34",("a","99")}
# b = {"2","PYTHON ","78",("n","88")}
# c = a.clear()
# print(c)

# a = {1,2,3,4,5,6}
# b = {3,4,5,6,7,8}
# c = a.issuperset(b)
# print(c)


# import random
# # a = random.randint(0,1000)   # 随机生成一个整数
# b = []   #用列表当容器时需要一个判断，用集合set()当容器时，不需要判断
# for x in range(0,10):
#     a = random.randint(0, 1000)
#     if a not in b:
#       b.append(a)
# print(b)

# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if( i != k ) and (i != j) and (j != k):
#              print (i,j,k)

# for a in range(101):
#     if a % 2 == 0:
#       print(a)

# 一张纸0.08mm 需要折多少次能超过珠穆朗玛峰（8848m）8848000mm
# a = 8848000
# b = 0.08
# c = 0
# while True:
#     c = c +1  #c=0时，开始进行第一次折叠，  当进行第二次折叠
#     b = b * 2  #这时这张纸的厚度为0.08*2=0.16，这时纸的厚度为0.16*2=0.32
#     if b > a:    #以此类推，当b大于a的时候，显示结果
#      print(c)
#      break  #终止循环


#冒泡排序
# a = input("输入一串数字:")
# b = a.split()
# c = len(b)
# for x in range(c):   # 大循环
#     for y in range(c-1):   #小循环，只能循环到倒数第二个，如果不减一，最后一个索引值无法和下一个比较，超出索引范围
#         if int(b[y]) > int(b[y+1]):
#             b[y],b[y+1] = b[y+1],b[y]
# print(b)



#选择排序
# a = input("输入一串数字:")
# b = a.split()
# c = len(b)
# for x in range(c):
#     for y in range(x+1,c):
#         if int(b[x]) > int(b[y]):
#             b[x],b[y] = b[y],b[x]
# print(b)



#考试题
# a = input("输入数字:")
# print(type(a))  #字符串类型
# b = 0
# while True:
#     b = b +1
#     if str(b) == a:
#         print(b)
#         print(type(b))   #数字类型
#         break

# a = eval("12345")
# print(type(a))


# #质数
# num = []
# c= 0
# for a in range(2,100):
#
#     for b in range(2,a):
#
#         if a % b == 0:
#
#
#             break
#         # c= c +a
#     else:
#         c = c + a
#     #         num.append(a)
# print(c)


#1-2+3-4+5... 奇加偶减
# x = 0
# for a in range(101):
#     if a % 2 == 0:
#         x = x -a
#     else:
#         x = x + a
# print(x)



# a = "Then one day the mother eagle appeared at the top of the mountain cliff, with a big bowl of delicious food and she looked down at her baby. The baby looked up at the mother and cried 'Why did you abandon me? I'm going to die any minute. How could you do this to me?'"

#1.统计字符串长度大于5的
# b = a.split()
# c = len(b)
# for x in b:
#     if len(x) > 5:
#         print(x)

# 2.将e全部替换成博文
# if a.find("e") != -1:
#     print(a.replace("e","博文"))

#3.截取第一个逗号前的所有单词，并将首字符大写
# x = a.split(",")   #以逗号分隔
# y = x[0]          #利用索引取第一个
# print(y.title())
#

#4.删除除包含英文o的单词









# d = {
#     "data": {
#         "msg":
#         [ gt5858cf6yh
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

# 1.求国家的个数
# x = d["data"]  #取出data后面的值
# y = x["msg"]   #去除msg后面的值
# z = set()
# for i in y:
#     j = i["country"]  #取出country后面的值
#     z.add(j)   #放到z集合里
# print(len(z))
#
# 2.身高范围
# x = d["data"]   #取出字典d里面data键的值
# y = x["msg"]     #取出data字典里面msg的列表
# z = set()
# n = 0
# for i in y:
#     n = n +1
#     j = i[f"s_{n}"]   #显示每个列表
#     m = j[-1]        #取每个列表的最后一位
#     z.add(m)         #f放到z集合里
# print(min(z),max(z))
#
# 3.求男女比例
# x = d["data"]   #取出字典d里面data键的值
# y = x["msg"]     #取出data字典里面msg的列表
# z = []
# n = 0
# for i in y:
#     n = n +1
#     j = i[f"s_{n}"]   #显示每个列表
#     m = j[1]
#     z.append(m)
# d = z.count("男")
# f = z.count("女")
# h = d/f
# print(h)
#
# 4.求平均身高
# x = d["data"]   #取出字典d里面data键的值
# y = x["msg"]     #取出data字典里面msg的列表
# z = []
# n = 0
# for i in y:
#     n = n +1
#     j = i[f"s_{n}"]   #显示每个列表
#     m = j[-1]
#     z.append(m.replace("cm","") )#替换cm为空格
# print(z)
# w = 0
# for u in z:
#     w = w + int(u)
# print(w/len(z))
# print(t)
# # print(d)



#5.170cm-180cm之间学生的姓名
# x = d["data"]   #取出字典d里面data键的值
# y = x["msg"]     #取出data字典里面msg的列表
# n = 0
# for i in y:
#     n = n +1
#     j = i[f"s_{n}"]   #显示每个列表
#     m = j[-1]
#     v= m.replace("cm","")#替换cm为空格
#     if  170 <= int(v) <= 180:  #如果身高满足这个条件，
#         f = j[0]              #打印出名字
#         print(f)




# sb0 = ["海洛因", "冰毒", "大麻", "罂粟", "快乐水"]
# sb1 = [2000, 1500, 1000, 5000, 9999]
# kc0 = [500, 500, 500, 500, 500]
# hyh0 = [13300000000, 18800000000, 13000000000]
# je0 = [90000, 60000, 100000]
# while True:
#     import time
#     je1 = je0
#     kc1 = kc0
#     print("编号","\t","\t","商品","\t","\t","\t","单价","\t","\t","\t","库存")
#     for i1,i2 in enumerate(sb0):
#         print(i1+1,"\t","\t","\t",i2,"\t","\t","\t",sb1[i1],"\t","\t","\t",kc0[i1])
#     sb3 = input("继续购买商品输入m,退出请输入e:")
#     if sb3 == "e":
#         break
#     sb4 = int(input("请输入购买商品的编号:"))
#     sb17 = 0
#     while True:                         #商品编号输入错误则继续输入，对多输入3次
#         if sb4 > len(sb0):
#             print("您输入的商品编号错误")
#             sb17 += 1
#             if sb17 == 3:
#                 break
#             sb4 = int(input("请重新输入购买商品的编号:"))
#         else:
#             break
#     if sb17 == 3:
#         break
#     sb5 = int(input("请输入购买商品的数量:"))
#     if sb5 >= kc1[sb4-1]:               #判断购买商品是否超过库存数量
#         print("您购买的商品超出库存")
#         break
#     else:
#         sb14 = kc1[sb4-1] - sb5
#         kc1.pop(sb4-1)
#         kc1.insert(sb4-1, sb14)
#     sb6 = input("使用会员账号输入Y,不使用输入N:")
#     if sb6 == "Y":                          #判定是否使用会员
#         sb7 = int(input("请输入会员账号:"))
#         sb15 = 0
#         for sb16 in range(3):
#             if sb7 not in hyh0:
#                 print("您账号输入错误")
#                 sb15 += 1
#                 if sb15 == 3:
#                     break
#                 sb7 = int(input("请再次输入会员账号:"))
#             else:
#                 break
#         if sb15 != 3:
#             sb8 = sb1[sb4-1]*sb5
#             sb9 = hyh0.index(sb7)
#             time.sleep(1)
#             print(f"您的会员当前余额为 {je1[sb9]} 元")
#             time.sleep(1)
#             print(f"您购买的商品总价为 {sb8} 元")
#             time.sleep(1)
#             print("会员账号打九折")
#             time.sleep(1)
#             print(f"会员账号打折后价格 {sb8*0.9} 元")
#             sb10 = je1[sb9] - sb8
#             if sb10 <= 0:
#                 print("您的会员账户余额不足")
#                 break
#             je1.pop(sb9)
#             je1.insert(sb9,sb10)         #会员金额前去本次支付的金额
#             time.sleep(3)
#             print(f"结账后您的会员账户余额为 {sb10} 元")
#             sb13 = input("是否退出本次购买,退出请输入x:")
#             if sb13 == "x":
#                 print("交易完成")
#                 break
#             else:
#                 continue
#         else:
#             print("交易失败")
#             break
#     sb11 = sb1[sb4-1]*sb5
#     print(f"您本次需要支付 {sb11} 元")
#     sb18 = input("请确定是否继续支付,是Y，否N:")
#     if sb18 == "N":
#         break
#     print("支付成功")
#     time.sleep(1)
#     sb12 = input("是否退出本次购买,退出请输入大写X:")
#     if sb12 == "X":
#         print("交易完成")
#         break

# print(f"商品编号        商品名          价格        库存量\n   1            方便面          50           100 \n   2            火腿肠          20           100 \n   3            泡面            80           100 \n   4            面包            40           80 \n   5            凤椒泡爪        60           50 ")
# b = ["方便面","火腿肠","泡面","面包","凤椒泡爪"]
# c = ["50","20","80","40","60"]
# a = ["100","100","100","80","50"]
# cc = 0
# ff = 0
# gg = 0
# m = 1000
# g = input("输入1是购买，2是退出购物:")
# if g == "2":
#     exit()
# elif g == "1":
#     h = int(input("输入你想购买商品编号:"))
#     i = int(input("输入你想购买的数量"))
#     j = int(input("是否有会员没有请输入3，有卡请输入卡号:"))
#     if j == 3:
#         for aa,bb in enumerate(b):
#             cc += 1
#             if h == cc:
#                 for dd,ee in enumerate(c):
#                     ff += 1
#                     if cc == ff:
#                         for hh,ll in enumerate(a):
#                             gg += 1
#                             if ff == gg:
#                                 z = int(ee)*i
#                                 v = int(ll)-i
#                                 print(f"总消费{z}元,仓库库存剩余{v}")
#     elif j == 111111:
#         for aa,bb in enumerate(b):
#             cc += 1
#             if h == cc:
#                 for dd,ee in enumerate(c):
#                     ff += 1
#                     if cc == ff:
#                         for hh,ll in enumerate(a):
#                             gg += 1
#                             if ff == gg:
#                                 z = int(ee)*i
#                                 v = int(ll)-i
#                                 r = z*0.9
#                                 while True:
#                                     if r <= m:
#                                         print(f"刷卡成功，会员打九折，总消费{z*0.9}元,仓库库存剩余{v},会员卡剩余金额{m-r}元")
#                                         break
#                                     elif r >= m:
#                                         print("对不起余额不足，请您及时充值")
#                                         x = input("是否充值，充值请按1,返回请按2:")
#                                         if x == "2":
#                                             exit()
#                                         elif x == "1":
#                                             gg = int(input("请输入充值金额，冲值大于1000送充值金额的%7,充值大于10000送充值金额的%10:"))
#                                             if 1000 > gg > 0:
#                                                 m += gg
#                                                 print(f"本次充值{gg}元,卡上余额{m}元")
#                                             elif 1000 <= gg < 10000:
#                                                 zz = int(gg*0.07)
#                                                 m += gg + zz
#                                                 print(f"本次充值{gg}元,奖励{zz}元,卡上余额{m}元")
#                                             elif gg >= 10000:
#                                                 zz = int(gg * 0.1)
#                                                 m += gg + zz
#                                                 print(f"本次充值{gg}元,奖励{zz}元,卡上余额{m}元")
#                                             else:
#                                                 print("充值失败")
#             else:
#                 print(f"对不起输入有误")
#     else:
#         print(f"对不起输入有误")


# while True:
#     a=input("用户请选择:")
#     if a=="离开":
#         break
#     sp=["航母","坦克","导弹","飞机","氢弹"]
#     jg=[7500,5500,8500,10000,12000]
#     kc=[10,25,40,20,30]
#     print("编号","\t","\t","商品","\t","\t","\t","\t","价格","\t","\t","\t","库存","\t","\t","\t")
#     for i,j in enumerate(sp):
#         print(i,"\t","\t","\t",j,"\t","\t","\t","\t",jg[i],"\t","\t","\t",kc[i],"\t","\t","\t")
#     b = int(input("输入商品编号:"))
#     d = int(input("输入购买量"))
#     if d<=kc[b]:
#         c=d*jg[b]
#         x=input("请问是否使用会员卡:")
#         if x=="使用":
#              while True:
#                  if input("请输入会员卡号:")!= "001":
#                      print("卡号不存在，请重新输入")
#                  else:
#                      n=int("100000")
#                      print(f'账号正确，账号金额为{n}元，等待结账')
#                      c=c*0.95
#                      if (n-c)<0:
#                          print("对不起先生，您的余额不足")
#                          while True:
#                              if input("是否进行充值:")=="是":
#                                  print("请输入充值金额")
#                                  cz=int(input('充值金额:'))
#                                  n=n+cz
#                                  print(f"充值成功，卡上余额为{n}")
#                              else:
#                                  print(f'退出充值，当前余额为{n}')
#                                  n=n-c
#                                  print(f'交易成功，本次消费{c},账号余额为{n}')
#                                  break
#                                  break
#                      else:
#                           n=n-c
#                           print(f'交易完成，本次消费{c}元，账户余额{n}元')
#         else:
#             print(f'交易处理，共{c}元，请付款')
#             fk=int(input('付款:'))
#             if fk >c:
#                 zl=fk-c
#                 print(f'交易完成，本次消费{c}元，付款{fk}元，找零{zl}元')
#             else:
#                 print('付款金额不足，请选择人道毁灭')
#     else:
#         print("库存不足，交易失败")


# a = "12 23 45 67 78"
# b = a.split(" ")
#
# print(len(b[-1]))
# a =1
# b = 2
# c = 2
# a = b = c
# print(a)

# f = open(file="a.txt",mode="w",encoding="utf-8")
# f.write("hello python")
# a = f.read()
# print(a)
# f.close()

# a = [ "a","b","c"]
# f = open(file="a.txt",mode="w",encoding="utf-8")
# for x  in a:
#     # f.write(f"{x}\n")
#     f.write(x + "\n")
# f.close()


# def k(h):
#     f = open(file=h,mode="r",encoding="utf-8")
#     s = f.readlines(13)
#
#     b = []
#     for i in s:
#         b.append(i)
#
#     f.close()
#     return b
#
# print(k("a.txt"))

#
# a = [0]
# if a == None:
#     print(a)
#
# a= ["shbskdjbgkdsfb"]
# b = list(a)
# print(b)


#函数写冒泡
# def i(z):
#     b = z.split(" ")
#     c = len(b)
#     for x in range(c):
#         for y in range(c-1):
#             if int(b[y]) > int(b[y+1]):
#                 b[y],b[y+1] = b[y+1],b[y]
#     return b
# print(i("1 4 3 45 34 21 2"))



# class A(object):
#     def __init__(self,x):
#         for i in range(1,x):
#             c = 0
#             for j in range(1,i+1):
#                 if i%j == 0:
#                     c = c + 1


#写100以内的质数之和,冒泡排序，选择排序,去重
# class A(object):
#     def zhishu(self):
#         c = 0
#         for a in range(2,100):
#             for b in range(2,a):
#                 if a % b == 0:
#                     break
#             else:
#                 c = c + a
#         print(c)
#         # return c
#
#     def maopao(self):
#         a="13,2,45,46,1,32,23"
#         b=a.split(",")
#         c = len(b)
#         for x in range(c):
#             for y in range(c-1):
#                 if int(b[y]) > int(b[y+1]):
#                     b[y],b[y+1] = b[y+1],b[y]
#         print(b)
#         # return b
#
#     def xuanze(self):
#         a = "99,1,3,5,7,2,4,23,21,12,56,46"
#         b = a.split(",")
#         c = len(b)
#         for x in range(c):
#             for y in range(x+1,c):
#                 if int(b[x]) > int(b[y]):
#                     b[x],b[y] = b[y],b[x]
#         print(b)
#         # return b
#
#     def shuzi(self):
#         b = 0
#         a ="13532"
#         while True:
#             b = b +1
#             if str(b) == a:
#                 print(b)
#                 break

#     def quchong(self):
#         a = [1,1,2,2,3,4,5,6,4,5]
#         b=[]
#         for i in a:
#             if i not in b:
#                 b.append(i)
#         print(b)

# aa=A()
# aa.zhishu()
# aa.maopao()
# aa.xuanze()
# aa.shuzi()
# aa.quchong()
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{i}*{j}={i * j}\t", end="")
    print()





