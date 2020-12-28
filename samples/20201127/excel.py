import xlrd
workbook=xlrd.open_workbook('test_vlaue.xlsx')
sheet=workbook.sheet_by_name('Sheet1')
print(sheet.row_values(0))