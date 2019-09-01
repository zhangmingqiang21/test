with open(r'C:\Youku\data\shuju.txt','r',encoding='utf-8') as f:
    x = f.read()
    y = x.split("\n")
    # print(y)
def asd():
    s = []
    for i in y:
        j = i.split(",")
        k = tuple(j)
        s.append(k)
    return s
# for i in range(5):
#     a={"name":f'{i}',"age":f'{i+1}'}
#     print(a)