#python  套接字  socket
#作用 ：实现两个或者多个应用的数据传输

#服务端
import socket
import os
#指定服务器的IP地址  和监听端口号
ip_port=('127.0.0.6',9999)

#建立一个套接字，为了服务器与客户端传输信息
s = socket.socket()  #创建对象

#绑定服务器地址和端口号
s.bind(ip_port)

#设置最大连接数,数字为几 最多为几个连接
s.listen(5)

#提示服务器端已经开启
print('启动socket服务，等待连接...')

#scoket  自动控制拥塞控制,持续开启服务，除非手动关闭
c,address = s.accept()
#处理客户端发来的数据，首先接受客户端发来的数据
# c_data = c.recv(1024).decode('utf-8')  #设置最大接收量,以kb为单位
# print(c_data)
# print(address)

while True:
    # c, address = s.accept()

    c_data = c.recv(1024).decode('utf-8')
    print(f"客户端发送的信息:{c_data}")   #客户端向服务器发送的信息

    t1 = input("输入发送到客户端的信息:")    #服务器向客户端发送信息
    # print(c_data)
    if t1 == "1":
        break
    else:
        #发送信息给客户端
        #①先找到客户端
        #②使用sendall
        c.send(t1.encode())

#关闭服务器
s.close()









