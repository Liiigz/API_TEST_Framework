import os
from utils.excel_utils import ExcelUtils

excel_path=os.path.join(os.path.dirname(__file__),'..','data','testcase_info.xlsx')
sheet_name='Sheet1'
class TestcseDataUtils:
    def __init__(self):
        self.excel_data=ExcelUtils(excel_path,sheet_name)

    def conver_testcase_data_to_dict(self):
        testcase_dice={}
        for row_data in self.excel_data.get_all_value():
            testcase_dice.setdefault(row_data['用例编号'],[]).append(row_data)
        return testcase_dice

    def conver_testcase_data_to_list(self):
        all_data_lsit=[]
        for key,value in self.conver_testcase_data_to_dict().items():
            case_dict={}
            case_dict['case_id']=key
            case_dict['case_info']=value
            all_data_lsit.append(case_dict)
        return all_data_lsit

if __name__=='__main__':
    testcase=TestcseDataUtils()
    case_list=testcase.conver_testcase_data_to_list()
    print(case_list)
    # for t in case_list:
    #     print(t)
    # print(case_list[0]['case_info'][0]['请求参数(get)'])

