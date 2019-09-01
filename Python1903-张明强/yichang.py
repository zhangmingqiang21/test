#python异常处理
#一错误
#①语法错误   书写格式class、缩进
#②代码逻辑错误  导致python解释器无法编译解释，导致python报错

#二、异常捕获
#处理错误过程  称为异常处理
#①  try......except   最简单的异常处理
# try:
#     a = 1 / 0
#     print(a)
# except OverflowError:
#     print("int数值太大错误")
# except ZeroDivisionError:
#     print("0不能被除的错误")
# finally:
#     print("无论什么错误都输出")


#②try......    except......else
try:
    a = 1 / 1
    print(a)
except OverflowError:
    print("int数值太大错误")
except ZeroDivisionError:
    print("0不能被除的错误")
else:
    print("不存在异常输出")



























