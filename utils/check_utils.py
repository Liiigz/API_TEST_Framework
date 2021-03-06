import json
import requests
import re
class CheckUtils():
    def __init__(self,response_data):
        self.response_data=response_data
        self.check_rules = {
            '无':self.none_check,
            'json_key': self.key_check,
            'json_key_value': self.key_value_check,
            '正则比对': self.regexp_check
        }
        self.pass_result={
            'code': 0,
            'response_code': self.response_data.status_code,
            'response_reason': self.response_data.reason,
            'response_headers': self.response_data.headers,
            'response_body': self.response_data.text,
            'check_result':True
        }
        self.fail_result={
            'code': 1,
            'response_code': self.response_data.status_code,
            'response_reason': self.response_data.reason,
            'response_headers': self.response_data.headers,
            'response_body': self.response_data.text,
            'check_result': False
        }


    def none_check(self):
        return True

    def key_check(self,check_data):
        key_list=check_data.split(',')#切割后是列表
        tmp_result=[]
        for key in key_list:
            if key in self.response_data.json().keys():
                tmp_result.append(True)
            else:
                tmp_result.append(False)
        if False in tmp_result:
            return self.fail_result
        else:
            return self.pass_result

    def key_value_check(self,check_data):
        key_value_dict=json.loads(check_data)
        tmp_result=[]
        for key_value in key_value_dict.items():
            if key_value in self.response_data.json().items():
                tmp_result.append(True)
            else:
                tmp_result.append(False)
        if False in tmp_result:
            return self.pass_result
        else:
            return self.pass_result

    def regexp_check(self,check_data,):
        tmp_result=re.findall(check_data,self.response_data.text)
        if tmp_result:
            return self.pass_result
        else:
            return  self.fail_result

    def run_check(self,check_type,check_data):
        if check_type=='无' or check_data=='':
            return self.check_rules[check_type]()
        else:
            return self.check_rules[check_type](check_data)


if __name__=='__main__':
    session=requests.session()
    get_params={"grant_type":"client_credential",
                "appid":"wxb6807ba1b89130e1",
                "secret":"652d6c4b429791c80f0badbda6a00829"}

    response = session.get(url=" https://api.weixin.qq.com/cgi-bin/token",
                                params=get_params,
                                )
    response.encoding = response.apparent_encoding
    c=CheckUtils(response)
    v=c.run_check('正则比对','"access_token":"(.+?)"')
    print(v)

