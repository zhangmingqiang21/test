# 去重
# a = [1,1,2,2,3,3,4,4,5,5,6,6]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)

# a = [1,2,2,1,3,4,4,3,6,2,7,56]
# print(set(a))

#冒泡
# a=input("输入一串数字:")
# b=a.split(",")
# c=len(b)
# for i in range(c):
#     for j in range(c-1):
#         if int(b[j])>int(b[j+1]):
#             b[j],b[j+1]=b[j+1],b[j]
# print(b)

# 选择
# a= input("输入一串数字:")
# b=a.split()
# c=len(b)
# for i in range(c):
#     for j in range(i+1,c):
#         if int(b[i])>int(b[j]):
#             b[i],b[j]=b[j],b[i]
# print(b)


# a=1
# for b in range(1,10):
#     a=a*b
# print(a)

#一张纸折多少次超过珠穆拉马凤
# a =8843000
# b=0.08
# c=0
# while True:
#     c=c+1
#     b=b*2
#     if b > a:
#         print(c)
#         break

#1-2+3-4...  偶减奇加到100
# a=0
# for i in range(101):
#     if i%2==0:
#         a=a-i
#     elif i%2 != 0:
#         a = a + i
# print(a)

# c=0
# for a in range(2,101):
#     for b in range(2,a):
#         if a%b ==0:
#             break
#     else:
#         c=c+a
# print(c)

# 1-5的阶乘之和之和
# c=0
# b=1
# for a in range(1,6):
#     b=b*a
#     c=c+b
# print(c)


# a=1234
# b=0
# while  True:
#     b=b+1
#     if str(b) == str(a):
#         print(b)
#         break
#
# for a in range(1,10):
#     for b in range(0,10):
#         for c in range(0,10):
#             x = 100*a+10*b+c
#             y = a**3+b**3+c**3
#             if x == y:
#                 print(x)

