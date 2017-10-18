import re

password = 'jinqiu10yue!'
password2 = 'ljljkljlk1212ADFSDF!'

#regex = re.compile(r'\S{8,}')
regex = re.compile(r'[0-9]{1,}')
regex2 = re.compile(r'[A-Z]{1,}')
regex3 = re.compile(r'[a-z]{1,}')
m = regex.search(password)
m2 = regex2.search(password)
m3 = regex3.search(password)



if (m==None or m2==None or m3==None):
	print("验证不通过！")
else:
	print("验证通过！")
	print("m="+m.group())
	print("m2="+m2.group())
	print("m3="+m3.group())

param = '   hello  world!  '
#ss = myStrip(param)
#print(ss)
#regex = re.compile(r'\s*(\S+)\s*')
#m = regex.findall(param)
#print(m)

# 去掉字符串前后空格的正则表达式，去掉前面或者后面
regex = re.compile(r'^\s*|\s*$')
print(param)
print(regex.sub('',param))

# 去除字符中原来的字符
regex = re.compile('orld')
print(regex.sub('',param))

def myStrip(param,oldstr):
	if oldstr=='':
		regex = re.compile(r'^\s*|\s*$')
		temp = regex.sub('',param)
		print(temp)
		return temp
	else:
		regex = re.compile(oldstr)
		temp = regex.sub('',param)
		print(temp)
		return temp

myStrip(param,'')
