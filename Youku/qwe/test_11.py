# 城市列表
# import requests
# url = "http://v.juhe.cn/xianxing/citys"
# querystring = {"key":"1383269623700716b207c01f4f97c337"}
# headers = {
#     'User-Agent': "PostmanRuntime/7.15.2",
#     'Accept': "*/*",
#     'Cache-Control': "no-cache",
#     'Postman-Token': "3bae49cc-5a17-4f63-a255-00dc5b225df4,7037409b-98f3-40ef-b012-0934ef4ca5cc",
#     'Host': "v.juhe.cn",
#     'Cookie': "aliyungf_tc=AQAAAAF6zjXKnAUAL7k4cxTxUAy4Kwk2",
#     'Accept-Encoding': "gzip, deflate",
#     'Connection': "keep-alive",
#     'cache-control': "no-cache"
#     }
# response = requests.request("GET", url, headers=headers, params=querystring)
# print(response.text)



import requests,pytest
from until.readdata import asd
s = (asd())
#尾号限行查询
@pytest.mark.parametrize("y1,y2",s)
def test_1(y1,y2):
    url = "http://v.juhe.cn/xianxing/index"
    querystring = {"key":f'{y1}',"city":f'{y2}'}
    # print(type(querystring))
    headers = {
        'User-Agent': "PostmanRuntime/7.15.2",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "0a27e7c7-4017-448e-8912-04f7511bb6df,0468b0fa-20ae-44c6-94e7-0328ae809600",
        'Host': "v.juhe.cn",
        'Cookie': "aliyungf_tc=AQAAAAF6zjXKnAUAL7k4cxTxUAy4Kwk2",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    # print(response.text)
    try:
        assert '查询成功' in response.text
    except:
        assert '查询成功' not in response.text






