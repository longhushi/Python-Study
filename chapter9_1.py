import shutil,os,zipfile

shutil.copy('1.txt','a.txt')

#shutil.copytree('釜山行','bushanaa')

#shutil.move('a.txt','bushanaa')

#shutil.move('a.txt','E:\\eggs')

os.unlink('a.txt')

for folderName, subfolders, filenames in os.walk('E:\\delicious'):
	print('The current folder is '+folderName)

	for subfolder in subfolders:
		print('SUBFOLDER OF '+folderName+': '+subfolder)
	for filename in filenames:
		print('FILE INSIDE '+folderName+': '+filename)

	print(' ')

exampleZip = zipfile.ZipFile('E:\\设计稿.zip')
print(exampleZip.namelist())
exampleZip.extractall()
exampleZip.close()
