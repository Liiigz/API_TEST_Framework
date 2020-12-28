import re
# str1='{"access_token":${token}}'
# variable_list=re.findall('\\${\w+}',str1)
# print(variable_list)
# dict1={'token':'ABCD'}
# str1=str1.replace(variable_list[0],'"%s"'%dict1[variable_list[0][2:-1]])
# print(str1)

str2='{"name":${n},"age":${a}}'
dict2={'n':'xiaoming','a':18}
variable_list=re.findall('\\${\w+}',str2)
print(variable_list)
for i in variable_list:
    print(i)
#     str2=str2.replace(i,'"%s"'%dict2[i[2:-1]])
# print(str2)

