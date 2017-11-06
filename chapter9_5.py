#删除不需要的文件
import os,shutil

def findLargeFile(source):
	largeFiles = []
	for foldername,subfolders,filenames in os.walk(source):
		print('The current folder is:%s'%foldername)
		print('subfolders:%s'%subfolders)
		for filename in filenames:
			fullfilename = os.path.join(foldername,filename)
			print('fullfilename:%s'%fullfilename)
			size = os.path.getsize(fullfilename)
			print("size:%d"%size)
			if size>100*1024*1024:
				largeFiles.append(fullfilename)
	print('大文件列表:%s'%largeFiles)


findLargeFile("E:\\书")