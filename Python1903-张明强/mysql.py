""""
import pymysql   #导入mysql这个包
connect = pymysql.connect(
    host = "192.168.10.16" ,   #数据库所在的主机IP地址/域名【云服务器--mysql数据库】
    port = 3306,    #mysql的端口号
    user = "root",    #mysql的用户名
    password = "Mysql@111111",    #mysql的密码
    charset = "utf8",     #mysql的编码方式
    # database = "zmq" ,    #数据库名
)
"""








