import re
import os
import codecs

result = []

regex = re.compile(r'\d*')

for filename in os.listdir('E:\\数据科学代码\\正则表达式批量测试文件'):
	print(filename)
	f = open(os.path.join('E:\\数据科学代码\\正则表达式批量测试文件',filename),'r',encoding='gbk')
	content = f.read()
	f.close()
	print(content)
	result.append(regex.search(content).group())

print(result)

