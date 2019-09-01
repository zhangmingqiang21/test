#爬虫   spider，网络蜘蛛
#根据自己指定的规则，模拟浏览器，批量下载网络中的资
#①聚焦爬虫：只针对某个网站的资源爬取
# ②搜素爬虫 ：针对全网络的资源爬取（例如 百度搜素引擎）
#可以模拟浏览器的库  requests /  urllib2  /  urllib3   /httpclient
#筛选数据的模块   re /  bs4  /  xpath
import re
import requests
class Douban(object):
    def print_res(self):
        url='https://movie.douban.com/top250?start=0&filte='
        head={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Mobile Safari/537.36'}
        res = requests.get(url=url,headers=head)
        html = res.content.decode('utf-8')
        return html
    def guolv(self,html):
        s=re.compile('<img width="100" alt="(.*?)" src="(.*?)" class="">')
        s1=re.findall(s,html)
        return s1
        # print(s1)
        # patt = re.compile(r'<div class="hd">(.*?)</span>',re.S)
        # items= patt.findall(html)
        # titles=[]
        # for i in items:5
        #     cc = re.compile('span class="title">(.*)',re.S)
        #     ww=cc.findall(i)
        #     titles.append(ww[0])

        #
        # tu1 = re.compile(r'<div class="pic">(.*)</a>',re.S)   #大筛选
        # tu3 = tu1.findall(html)
        # lianjie=[]
        # for j in tu3:
        #     tu = re.compile('src="https://(.*?)"',re.S)    #小筛选
        #     xx = tu.findall(j)
        #     for jj in xx:
        #         yy = f'https://{jj[0]}.jpg'
        #         lianjie.append(yy)
        # return titles,lianjie
    def save(self,ziyuan):
        for i in ziyuan:
            res = requests.get(i[1])
            hhh = res.content
            with open(f'{i[0]}.jpg','wb') as f:
                f.write(hhh)

x = Douban()

htm=x.print_res()
# print(x.guolv(htm))
ziyuan = x.guolv(htm)
x.save(ziyuan)
# <img src="https://img3.doubanio.com/view/photo/m/public/p480747492.webp">




