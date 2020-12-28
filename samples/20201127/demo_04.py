import json

json_obj={"access_token":"40_k","expires_in":7200}
except_str='{"expires_in":7200,"access_token":"40_k"}'
except_dict=json.loads(except_str)
print(except_dict.items())
print(list(except_dict.items()))
print(json_obj.items())
#单项
# if  list(except_dict.items())[0] in list(json_obj.items()):
#     print('true')
#多项
yes_no=[]
for i in except_dict.items():
    if i in except_dict.items():
        yes_no.append(True)
    else:
        yes_no.append(False)
if  False in yes_no:
    print('false')
else:
    print('true')