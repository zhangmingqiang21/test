# var = "A目录下的aa.py"
#
# def k():
#     print(var)



# import xlwt
# # 新建一个excel文件
# d = xlwt.Workbook()
# # 新建一个excel表     .add_sheet("表名")必填
# table = d.add_sheet("表一")
# # 写入数据到excel表中
# # 一次写一个单元格   .write(行索引值,列索引值,"数据")
# table.write(0,0,"张三")
# # 保存文件   .save("文件名")
# d.save("b.xls")

# 读取Excal表格
#python 操作 Excel 表格
# import xlrd
# d = xlrd.open_workbook(filename="a.xls")
#获取Excel表,返回的是一个包含所有Excel的列表
#假设文件中存在两个Excel表，那么列表中['sheet1','sheet2']
#打开所有表
# table = d.sheets()
#打开索引值对应的表
# table = d.sheets()[0]
#获取表中的数据   row_values() 获取整行的数据，必须制定获取的行号
# x = table.row_values(0)
# y = table.row_values(0,2)       #获取某行的某索引列之后的数据，包括索引列
# z = table.row_values(0)[0]      #获取某行的某个索引的数据
# print(x)
#获取某个单元格的值,先通过row()获取某一行 ---> 返回一个列表
#在通过列表的索引获取到元素 ---> .value获取到具体的值
# dan = table.row(0)[0].value
# print(dan)
#获取表格中的某一列中的某个元素
# list = table.col(0)[1].value       #table.col()[].value ---> table.col_values()[]
# print(list)
#获取表格中的某一行的某一列
# dan2 = table.cell(0,0).value    #
# print(dan2)
#获取行数
# h = table.nrows
# print(h)
#获取列数
# l = table.ncols
# print(l)
#通过行数获取所有数据
# for i in range(h):
#     print(table.row_values(i))
#获取表格中的某一列
# b = table.col_values(1)
# print(b)
#通过列数获取所有数据
# for j in range(l):
#     print(table.col_values(j))
#打印/输出Excel表的名字
#d:打开的Excel文件   #sheet_names():找出文件中所有表的名字
# print(d.sheet_names())
#通过索引值获取表
#假设一个文件中存在两个表，sheet1和sheet2，
#使用sheet_by_index(0) --> 打开的是sheet1
# table = d.sheet_by_index(0)
# print(table)












