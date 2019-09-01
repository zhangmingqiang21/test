#客户端
import socket
#指定客户端ip，目的端口号
ip_port=('127.0.0.6',9999)

#创建一个套接字，目的接受服务器发送的数据
c1 = socket.socket()

#连接服务器
c1.connect(ip_port)


while True:
    t = input("客户端发送给服务器的信息:")
    #设置一个条件跳出死循环
    if t == "1":
        break
    else:
        print(f"客户端向服务器发送的信息:")
        c1.sendall(t.encode())
        s_data = c1.recv(1024).decode('utf-8')   #处理服务器已经发送到客户端上的信息
        print((s_data))
# c,address = c1.accept()
# c_data = c.recv(1024).decode('utf-8')
# print(c1_data)
c1.close()





