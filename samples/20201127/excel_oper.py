import xlrd
# workbook = xlrd.open_workbook('C:\\Users\\BTI-PC-Z66133-008\\Desktop\\test_vlaue.xlsx')
# sheet = workbook.sheet_by_name('Sheet1')

workbook=xlrd.open_workbook('test_vlaue.xlsx')
sheet=workbook.sheet_by_name('Sheet2')
a=sheet.ncols
print(a)

# 输出一个单元格的值
def get_cell_value(row,col):
    for row_min,row_max,col_min,col_max in sheet.merged_cells:
        if row_min <= row < row_max:
            if col_min<= col < col_max:
                cell_value=sheet.cell_value(row_min,col_min)
                break
            else:
                cell_value=sheet.cell_value(row,col)
        else:
            cell_value=sheet.cell_value(row,col)
    return cell_value

# 输出所以单元格的值

 for i in range(sheet.nrows):
    for j in range(sheet.ncols):
         value=get_cell_value(i, j)
         print(value,end=' ')
    print()

# 以行为单位，将每行数据以字典的形式放在一个列表中
def get_all_value():
    row_value=[]
    row_head=sheet.row_values(0)
    for i in range(1,sheet.nrows):
        row_dict = {}
        for j in range(sheet.ncols):
            row_dict[row_head[j]] = get_cell_value(i, j)
        row_value.append(row_dict)
    return row_value

data_list=[{'事件': '学习python编程', '步骤序号': 'step_01', '步骤操作': '购买微课', '完成情况': 100.0}, {'事件': '学习python编程', '步骤序号': 'step_02', '步骤操作': '根据微课搭建好环境', '完成情况': 100.0}, {'事件': '学习python编程', '步骤序号': 'step_03', '步骤操作': '做好笔记', '完成情况': 100.0}, {'事件': '学习python编程', '步骤序号': 'step_04', '步骤操作': 'python应用', '完成情况': 100.0}, {'事件': '学习java编程', '步骤序号': 'step_01', '步骤操作': '购买微课', '完成情况': 100.0}, {'事件': '学习java编程', '步骤序号': 'step_02', '步骤操作': '根据微课搭建好环境', '完成情况': 100.0}, {'事件': '学习java编程', '步骤序号': 'step_03', '步骤操作': '做好笔记', '完成情况': 100.0}, {'事件': '学习java编程', '步骤序号': 'step_04', '步骤操作': 'java应用', '完成情况': 100.0}]
data_dict = {}
for d in data_list:
    data_dict.setdefault(d['事件'],[]).append(d)
print(data_dict)
