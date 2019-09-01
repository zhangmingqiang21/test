#写入excal表格
# import xlwt
# d=xlwt.Workbook()
# table=d.add_sheet("表1")
# for i in range(1,10):
#     for j in range(1,i+1):
#         table.write(i-1,j-1,f"{j}*{i}={j*i}")
# d.save("aa.xls")

#读取excal表格
# import xlrd
# d=xlrd.open_workbook(filename="aa.xls")
# table=d.sheets()[0]
# row=table.row_values(0)
# # print(row)
# col=table.col_values(0)
# # print(col)
# x=table.nrows
# y=table.ncols
# for i in range(x):
#     print(table.row_values(i))
# for j in range(y):
#     print(table.col_values(j))

#操作txt文档
# import xlwt
# d=open(file="a.txt",mode="r",encoding="utf-8")
# d1=xlwt.Workbook()
# table=d1.add_sheet("表1")
# # for i in range(1,11):
# x=d.read()
# for i in range(0,10):
#     table.write(i,0,x)
# d1.save("aa.xls")

#写入excal表格
# import xlwt
# d=xlwt.Workbook()
# table=d.add_sheet("111")
# for i in range(0,11):
#     table.write(i,0,"x\n")
# d.save("m.xls")





