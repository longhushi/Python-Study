import os

print(os.path.join('usr','bin','spam'))

myFiles = ['accounts.txt','details.csv','invite.docx']
for filename in myFiles:
	print(os.path.join('C:\\Users\\asweigart',filename))

print(os.getcwd())

#os.chdir('D:\\')
#print(os.getcwd())

#os.makedirs('E:\\delicious\\waffles')

print(os.path.abspath('.'))
print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))

print(os.path.relpath('C:\\Windows','C:\\'))

path = 'C:\\Windows\\System32\\calc.exe'
print(os.path.basename(path))
print(os.path.dirname(path))

print(path.split(os.path.sep))
print('/usr/bin'.split(os.path.sep))

print(os.path.getsize('E:\\数据科学代码'))
print(os.listdir('E:\\数据科学代码'))

totalSize = 0
for filename in os.listdir('F:\\游戏'):
	print(filename)
	totalSize = totalSize + os.path.getsize(os.path.join('F:\\游戏',filename))
print(totalSize)

import shelve

shelfFile = shelve.open('mydata')
cats = ['Zophie','Pooka','Simon']
shelfFile['cats'] = cats
#shelfFile.close()

type(shelfFile)
print(shelfFile['cats'])
shelfFile.close()