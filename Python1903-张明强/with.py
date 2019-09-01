#with语句的应用场合：主要操作系统资源，建立连接，python线程，进程的关闭释放
#with  一种概念    上下文管理

# import xlrd
# with open("py1.txt","r",encoding="utf8")  as fb:
#     a = fb.read()
#     print(a)



#python的正则表达式  re
#正则只能匹配字符串
#    re.S  给点加功能的，让点可以匹配到包括换行符在内的任意字符
#     re.I   让正则表达式不区分大小写
# .  匹配任意一个字符  ，除了换行符
#  *  匹配前一次字符0次或多次
#  +  匹配前一个字符一次或多次
# ？  匹配前一个字符0次或1次
#  ^ 匹配以某个字符串开头的
#  $   匹配以某个字符串结尾的
#  {m}  匹配括号内字符出现的指定的次数
#   {m,n}   匹配最少m次，最多n次
#  []    匹配括号内任意一个字符，每个字符只匹配一次
#  |  匹配左右两个表达式
#  \D  匹配不是十进制数字的字符
#  \   匹配十进制数字的字符
#  \s   匹配空白字符，\t \n \f  \v
#  \S   匹配非空白字符的任意字符
import re
# s = " 21323 34567189"
# #编译正则表达式  有几个点就是匹配几个字符，从左向右
# x = re.compile('\n')
# #匹配正则  第一个是编译的正则表达式，第二个是字符串
# res = re.match(x,s)
# print(res)
#
# j = "http://www.baidu.com"
# b = re.compile('http://.(.*).com')
# res = re.findall(b,j)
# print(res)


#search  正则表达式，要匹配字符串


#从左向右对整个字符串进行搜索匹配
#匹配不到返回None，匹配到第一个就停止匹配

#findall  对字符串进行一个搜索，从左向右搜索，匹配到的内容存放到列表里
#如果使用小括号，则仅匹配小括号里面的内容


#贪婪模式  .*   尽可能多的匹配字符

#非贪婪模式  .*?   匹配到字符就停止




#sub
# a = "hello python"
# b = re.sub('l','kk',a)    #第一个为需要换的字符，第二个替换后的字符，
# print(b)

# f = '1234567890'
# b = re.sub('1','1,',f)
# print(b)


#水仙花数
# for a in range(1,10):
#     for b in range(0,10):
#         for c in range(0,10):
#             x = a*100+b*10+c
#             y = a**3+b**3+c**3
#             if x == y:
#                 print(x)


# 1234可以组成多少数字
# a = [1,2,3,4]
# for i,j,k,m in a:
#     for j in a:
#         for k in a:
#             for m in a:
#                 if i != j != k != m:
#                      print(i,j,k,m)




# a =input("输入一串数字:")
# b=0
# while True:
#     b = b + 1
#     if str(b) == str(a):
#         print(b)
#         break
#