import requests
import re
str='{   "tag":{ "id":134, "name":"广东"   } } '
v=re.findall('"id":(.+?),',str)[0]
print(v)
print(type(v))
