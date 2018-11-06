import re
str1 = '3364成功'
pattern = re.compile(r'[^\d]*(\d+)[^\d]*')
res = re.findall(pattern, str1)
print(res)