#python发email邮件
#使用到的模块  smtplib  email
import smtplib

from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
class A(object):
    def hehe(self):

        #设置服务器所需要的信息
        #邮件服务器地址
        mail_host = "smtp.163.com"

        #用户名
        mail_user="JSDU0820@163.com"

        #客户端授权码或者密码
        mail_pass="qwe54188"

        #设置服务器端口号

        mail_port=465

        #y邮件发送方的地址
        sen ="JSDU0820@163.com"

        #接收方的地址,可以写多个
        rec="xu17868801452@163.com"

        #设置邮件主题
        sub = '<12>'

        #设置邮件正文
        con= 'aknfd,sdn'

        #三个参数:第一个是文本内容，第二个是plain 文本格式，第三个是utf-8  编码方式
        mes= MIMEText(con,'plain','utf-8')

        #发送邮件是填写收件人。发件人，主题
        #发送信息
        mes['From']=Header(sen)

        #接收方信息
        mes['to']=Header(str(":".join(rec)))

        #主题绑定
        mes['Subject']=Header(sub)

        #登陆并发送邮件
        try:
            #第一步：登录到自己的邮箱
            smtpobj = smtplib.SMTP_SSL(host=mail_host,port=mail_port)

            #输入密码 登陆到服务器
            smtpobj.login(user=mail_user,password=mail_pass)

            #发送邮件的方法as.string 以字符串的形式发送出去
            smtpobj.sendmail(
                sen,rec,mes.as_string())

            #退出邮箱
            smtpobj.quit()
            print("已发送")
        except smtplib.SMTPException as e:
            #打印错误
            print("发送失败",e)

        #添加附件需要一个类MIMEMultipart  ，将正文及附件添加到邮件里
        # mes1=MIMEMultipart()
        # mes1['From']=Header(sen);
        # mes1['to']=Header(str(":".join(rec)))
        # mes1['Subject'] = Header(sub)
        #
        # #使用html格式的正文内容，添加附件
        # with open('acc.html','r') as h:
        #     con2=h.read()
        #
        # #设置html格式参数
        # part1=MIMEText(con2,'html','utf-8')
        #
        # #设置txt参数
        # part2 = MIMEText(con2,'plain','utf-8')
        #
        # # 附件设置内容类型，方便起见，设置为二进制流
        # part2['Content-Type'] = 'application/octet-stream'
        # # 设置附件头，添加文件名
        # part2['Content-Disposition'] = 'attachment;filename="abc.txt"'
        #
        # #添加照片附件
        # with open('mn.png','rb') as fp:
        #     #MIMEImage 加载二进制图片，用于附件传输
        #     pic= MIMEImage(fp.read())
        # pic['Content-Type']='application/octet-stream'
        # pic['Content-Disposition']='attachment;'
aa=A()
aa.hehe()






