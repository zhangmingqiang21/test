class A(object):
    def jj(self):
        for i in range(1, 10):
            for j in range(1, i):
                print(f"{i}*{j}={i*j}\t",end="")
            print()
    def zhishu(self,x):
        c = 0
        for a in range(2,x):
            for b in range(2,a):
                if a % b == 0:
                    break
            else:
                c = c + a
        print(c)
    def jc(self,x):
        b=1
        c=0
        for a in range(1,x+1):
            b=b*a
            c=c+b
        print(c)
    def sanjiao(self):
        a = int(input("输入第一个数字:"))
        b = int(input("输入第二个数字:"))
        c = int(input("输入第三个数字:"))
        if a + b <= c or a + c <= b or b + c <= a:
            print("不是三角形")
        elif a == b and b == c:
            print("正三角形")
        elif a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2:
            print("直角三角形")
        elif a == b or b == c or a == c:
            print("等腰三角形")
        elif a ** 2 + b ** 2 > c ** 2 or a ** 2 + c ** 2 > b ** 2 or b ** 2 + c ** 2 > a ** 2:
            print("锐角三角形")
        elif a ** 2 + b ** 2 < c ** 2 or a ** 2 + c ** 2 > b ** 2 or b ** 2 + c ** 2 < a ** 2:
            print("钝角三角形")
    def qc(self):
        a=input("输入一串数字:")
        x =a.split()
        b=[]
        for c in x:
            if c not in b:
                b.append(c)
        # print(b)   去重后的结果
        d = len(b)
        for i in range(d):
            for j in range(i+1,d):
                if int(b[i])>int(b[j]):
                    b[i],b[j]=b[j],b[i]
        print(b)
    def huiwen(self):
        a=input("输入一串字符串:")
        b=len(a)
        c=1
        for i in range(b):
            if a[i] == a[-(i+1)]:
                pass
            else:
                c = c+1
        if c == 1:
            print(f"{a}是回文")
        else:
            print(f"{a}不是回文")
    def xuanze(self):
        a=input("输入一串数字:")
        b=a.split()
        c=len(b)
        for i in range(c):
            for j in range(i+1,c):
                if int(b[i])>int(b[j]):
                    b[i],b[j]=b[j],b[i]
        print(b)
    def maopao(self):
        a = input("输入一串数字:")
        b = a.split()
        c = len(b)
        for i in range(c):
            for j in range(c-1):
                if int(b[j])>int(b[j+1]):
                    b[j],b[j+1]=b[j+1],b[j]
        print(b)
    def hua(self):
        for a in range(1,10):
            for b in range(0,10):
                for c in range(0,10):
                    x = 100*a + 10*b + c
                    y = a**3 + b**3 + c**3
                    if x == y:
                        print(x)
    def shuzi(self):
        a=input("输入一串字符串:")
        b=0
        while True:
            b=b+1
            if str(b) == str(a):
                print(b)
                break

    def zuc(self):
        a = input("输入四个数字:")
        b = a.split()
        for x in b:
            for y in b:
                for z in b:
                    if x!=y and y!=z and z!=x:
                        print(x,y,z)
    def nuo(self):
        a=input("输入一串数字:")
        b=a.split()
        c=len(b)
        for i in range(c-1):
            b[i],b[i-1]=b[i-1],b[i]
        print(b)
    def yinshu(self):
        x = 0



qq=A()
qq.jj()
# qq.zhishu(200)
# qq.jc(5)
# qq.sanjiao()
# qq.qc()
# qq.huiwen()
# qq.xuanze()
# qq.maopao()
# qq.hua()
# qq.shuzi()
# qq.zuc()
# qq.nuo()
# qq.yinshu()





