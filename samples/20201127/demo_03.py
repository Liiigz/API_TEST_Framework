import json

str='{"access_token":"40_LrSQxY-Z94lll2N44R83lhX9nAf2BB5ZEetuVlkoM9AzMwu-gMF_uhkjOtQ6b2pYSmUisrbK6sbBQSzpEc4cKXvkBpCZGcz9GF1HkbGD6_2s-x5V7hQae4BBBsuKSLX1sFJKNmWeRlRtvSlWCDOgAEAYZK","expires_in":7200}'
json_obj=json.loads(str)
print(type(json_obj))
#检查key是否存在
if "access_token" in json_obj.keys():
    print('True')
else:
    print('False')

#检查多个key是否存在
check_keys=["access_token","expires_in"]
yes_no=[]
for check_key in check_keys:
    if check_key in json_obj.keys():
        yes_no.append(True)
    else:
        yes_no.append(False)
if  False in yes_no:
    print('False')