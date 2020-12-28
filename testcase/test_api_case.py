import paramunittest
import os
import unittest
from utils.testcase_data_utils import TestcseDataUtils
from utils.request_utils import RequestUtils
import warnings

test_case_lists=TestcseDataUtils().conver_testcase_data_to_list()
print(test_case_lists)
@paramunittest.parametrized(
    *test_case_lists
)
class TestApiCase(paramunittest.ParametrizedTestCase):
    def setUp(self) -> None:
        warnings.simplefilter('ignore',ResourceWarning)#(过滤掉警告)
    def setParameters(self, case_id, case_info):
        self.case_id=case_id
        self.case_info=case_info

    def test_api_case(self):
        self._testMethodName=self.case_step[0].get('测试用例编号')
        self._testMethodDoc=self.case_step[0].get('测试用例名称')
        test_reult=RequestUtils().request_by_step(self.case_info)
        self.assertTrue(test_reult['check_result'])

if __name__=='__main__':
    unittest.main(verbosity=2)
