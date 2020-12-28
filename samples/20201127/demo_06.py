import re
str1='{"access_token":"40_FMacslAAjdKmROpPo1oC4eKJXdKWuzoUftLwIjiak9PEmCj_Vgmr43a_Vqh1Ju0A2UAzdKVe17-DVnQ6LFUQjdjnUjUQghLyfOgS0fzhbRpu8sQOZkNysjY6vP5erWwLBB8COcjqGaZufrEQPWXhAJASZA","expires_in":7200}'
str2='"access_token":"(.+?)"'
v=re.findall(str2,str1)
print(v)
if v:
    print(True)
else:
    print(False)
