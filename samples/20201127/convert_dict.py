#coding:utf-8
import requests
from utils.config_utils import local_config
import ast
import json
import jsonpath
import re
class RequestUtils():
    def __init__(self):
        self.hosts=local_config.HOSTS
        self.session=requests.session()
        self.tmp_variables={}

    def get(self,requests_info):
        url=self.hosts+requests_info['请求地址']
        variable_list=re.findall('\\${\\w+}',requests_info['请求参数(get)'])
        for v in variable_list:
            requests_info['请求参数(get)']=requests_info['请求参数(get)'].replace(v,'"%s"'%self.tmp_variables[v[2:-1]])
        response=self.session.get(url=url,
                                  params=json.loads(requests_info['请求参数(get)']),
                                  headers=requests_info['请求头部信息']
                                  )
        response.encoding = response.apparent_encoding
        if requests_info['取值方式']=='jsonpath取值':
            value=jsonpath.jsonpath(response.json(),requests_info['取值代码'])[0]
            self.tmp_variables[requests_info['取值变量']]=value
        elif requests_info['取值方式']=='正则取值':
            value=re.findall(requests_info['取值代码'],response.text)[0]
            self.tmp_variables[requests_info['取值变量']] = value
        result={
            'code':0,
            'response_code':response.status_code,
            'response_reason':response.reason,
            'response_headers':response.headers,
            'response_body':response.text
        }
        return result

    def post(self,requests_info):
        url = self.hosts + requests_info['请求地址']
        get_variable_list = re.findall('\\${\\w+}', requests_info['请求参数(get)'])
        for v in get_variable_list:
            requests_info['请求参数(get)'] = requests_info['请求参数(get)'].replace(v, '"%s"' % self.tmp_variables[v[2:-1]])
        post_variable_list = re.findall('\\${\\w+}', requests_info['请求参数(post)'])
        for v in post_variable_list:
            requests_info['请求参数(post)'] = requests_info['请求参数(post)'].replace(v, '"%s"' % self.tmp_variables[v[2:-1]])
        response = self.session.post(url=url,
                                    params=json.loads(requests_info['请求参数(get)']),
                                    headers=requests_info['请求头部信息'],
                                    json=json.loads(requests_info['请求参数(post)'])
                                    )
        response.encoding = response.apparent_encoding
        if requests_info['取值方式']=='jsonpath取值':
            value=jsonpath.jsonpath(response.json(),requests_info['取值代码'])[0]
            self.tmp_variables[requests_info['取值变量']]=value
        elif requests_info['取值方式']=='正则取值':
            value=re.findall(requests_info['取值代码'],response.text)[0]
            self.tmp_variables[requests_info['取值变量']] = value
        result = {
            'code': 0,
            'response_code': response.status_code,
            'response_reason': response.reason,
            'response_headers': response.headers,
            'response_body': response.text
        }
        return result

    def request(self,step_info):
        request_type=step_info['请求方式']
        if request_type=='get':
            result=self.get(step_info)
        elif request_type=='post':
            result=self.post(step_info)
        else:
            result={'code':1,'result':'请求方式不支持'}
        print(self.tmp_variables)
        return result

    def request_by_step(self,test_steps):
        for test_step in test_steps:
            result=self.request(test_step)
            if result['code'] !=0:
                break
        return result






if __name__=='__main__':
    # post_dict={'用例编号': 'api_case_03', '测试用例名称': '删除标签接口测试', '用例执行': '是', '用例步骤': 'step_03', '接口名称': '删除标签接口', '请求方式': 'post', '请求头部信息': '', '请求地址': '/cgi-bin/tags/delete', '请求参数(get)': '{"access_token":"40_PoEuGpT4_Lag57Cr5-v2DGgljp3n90mjMND558GOxfv9zWQnS5nClqaXnthWTUEbSZY9ySXXscP-K9vL9dJrqcnGLc6htRhAWMaM9vF1bcy3Qteg5Lc5w1DBi0c7NsVv1cyOCQ7UcC3EskN0ITDhADARCM"}', '请求参数(post)': '{   "tag":{        "id" : 120} }', '取值方式': '无', '取值代码': '', '取值变量': ''}
    # step_info=[{'用例编号': 'api_case_02', '测试用例名称': '创建标签接口测试', '用例执行': '是', '用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求头部信息': '', '请求地址': '/cgi-bin/token', '请求参数(get)': '{"grant_type":"client_credential","appid":"wxb6807ba1b89130e1","secret":"652d6c4b429791c80f0badbda6a00829"}', '请求参数(post)': '', '取值方式': '正则取值', '取值代码': '"access_token":"(.+?)"', '取值变量': 'token'},  {'用例编号': 'api_case_02', '测试用例名称': '创建标签接口测试', '用例执行': '是', '用例步骤': 'step_02', '接口名称': '创建标签接口', '请求方式': 'post', '请求头部信息': '', '请求地址': '/cgi-bin/tags/create', '请求参数(get)': '{"access_token":${token}}', '请求参数(post)': '{   "tag" : {     "name" : "T1"   } } ', '取值方式': '无', '取值代码': '', '取值变量': ''}]
    step_info=[{'用例编号': 'api_case_03', '测试用例名称': '删除标签接口测试', '用例执行': '是', '用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求头部信息': '', '请求地址': '/cgi-bin/token','请求参数(get)': '{"grant_type":"client_credential","appid":"wxb6807ba1b89130e1","secret":"652d6c4b429791c80f0badbda6a00829"}', '请求参数(post)': '', '取值方式': 'jsonpath取值', '取值代码': '$.access_token', '取值变量': 'token'},{'用例编号': 'api_case_03', '测试用例名称': '删除标签接口测试', '用例执行': '是', '用例步骤': 'step_02', '接口名称': '创建标签接口', '请求方式': 'post','请求头部信息': '', '请求地址': '/cgi-bin/tags/create', '请求参数(get)': '{"access_token":${token}}','请求参数(post)': '{   "tag" : {     "name" : "T3"   } } ', '取值方式': '正则取值', '取值代码': '"id":(.+?),','取值变量': 'tag_id'},{'用例编号': 'api_case_03', '测试用例名称': '删除标签接口测试', '用例执行': '是', '用例步骤': 'step_03', '接口名称': '删除标签接口', '请求方式': 'post','请求头部信息': '', '请求地址': '/cgi-bin/tags/delete', '请求参数(get)': '{"access_token":${token}}','请求参数(post)': '{   "tag":{        "id" : ${tag_id}  } } ', '取值方式': '无', '取值代码': '', '取值变量': ''}]
    v=RequestUtils()
    v.request_by_step(step_info)
