import requests
session=requests.session()
response=session.get(url='http://www.hnxmxit.com/')
print(response.headers)#charset=utf-8  若没有此字节，则默认编码格式为iso-8859-1
response.encoding=response.apparent_encoding#网页的内容中分析网页的编码格式
print(response.text)