# 遍历一个目录，查找特定扩展名的文件，拷贝到一个新的文件夹中
import shutil,os

def findAndCopy(source,dest):
	for folderName,subfolders,filenames in os.walk(source):
		print('folderName:%s'%folderName)
		print('subfolders:%s'%subfolders)
		for filename in filenames:
			print("filename:%s"%filename)
			base = os.path.basename(filename)
			print("basename%s"%base)
			if(('jpg' in base) or ('pdf' in base)):
				fullname = os.path.join(folderName,filename)
				shutil.copy(fullname,dest)

findAndCopy('E:\\书\\口琴','E:\\temp')
