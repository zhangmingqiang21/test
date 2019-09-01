# json  是一种轻量级的数据交互格式
# JavaScript 语言中的一种数据表现形式
# python 中没有json
import json
import re,requests
# 将json字典转化为字符串  [json.dumps]
"""
a={"name":111,"age":222}
print(type(a))
b=json.dumps(a)
print(type(b))
"""

# 将json字符串转化为字典     [json.loads]
"""
a={"name":111,"age":222}
print(type(a))
b=json.dumps(a)
print(type(b))
c=json.loads(b)
print(type(c))
"""
url="https://www.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=1&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=12&city=410200&geoobj=114.215104%7C34.722586%7C114.577653%7C34.877078&_src=around&keywords=%E7%BE%8E%E9%A3%9F"
a=requests.get(url)
b=a.json()
print(b['rgv587_flag'])

