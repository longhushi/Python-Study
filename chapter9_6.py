# 消除缺失的编号
import os,shutil,re

def rangeFile(source,perfix):
	i = 1
	for foldername,subfolders,filenames in os.walk(source):
		for filename in filenames:
			if filename.startswith(perfix):
				regex = re.compile(r'.*?(\d+)')
				m = regex.search(filename)
				n = m.group(1)
				print('n='+n)
				num = int(n)
				if num!=i:
					num = i
					if num<10:
						name = perfix+'00'+str(num)
					elif num<100:
						name = perfix+'0'+str(num)
					else:
						name = perfix+str(num)
					new = regex.sub(name,filename) # 用正则表达式替换数字
					print('new:%s'%new);
					newname = os.path.join(foldername,new)
					oldname = os.path.join(foldername,filename)
					print('oldname:%s'%oldname)
					print('newname:%s'%newname)
					shutil.move(oldname,newname)
				i+=1

rangeFile('E:\\delicious','spam')

