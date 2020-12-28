import xlrd
import os

excel_current_path=os.path.join(os.path.dirname(__file__),'..','data','excel_data.xlsx')
class ExcelUtils():
    def __init__(self,excel_path,sheet_name):
        self.excel_path=excel_path
        self.sheet_name=sheet_name
        workbook=xlrd.open_workbook(self.excel_path)
        self.sheet=workbook.sheet_by_name(self.sheet_name)

    def get_row_count(self):
        row_count=self.sheet.nrows
        return row_count

    def get_col_count(self):
        col_count=self.sheet.ncols
        return  col_count

    def get_metge_cell_value(self,row_index,col_index):
        cell_value=None
        for row_min, row_max, col_min, col_max in self.sheet.merged_cells:
            if row_min <= row_index < row_max:
                if col_min <= col_index < col_max:
                    cell_value = self.sheet.cell_value(row_min, col_min)
                    break
                else:
                    cell_value = self.sheet.cell_value(row_index, col_index)
            else:
                cell_value = self.sheet.cell_value(row_index, col_index)
        return cell_value

    def get_all_value(self):
        row_value = []
        row_head = self.sheet.row_values(0)
        for i in range(1, self.get_row_count()):
            row_dict = {}
            for j in range(self.get_col_count()):
                row_dict[row_head[j]] = self.get_metge_cell_value(i, j)
            row_value.append(row_dict)
        return row_value



if __name__=='__main__':
    c=ExcelUtils(excel_current_path,'Sheet1')
    print(c.get_all_value())

