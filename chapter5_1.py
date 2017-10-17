import pprint

spam = {'color':'red','age':42}
for v in spam.values():
	print(v)

for k in spam.keys():
	print(k)

for i in spam.items():
	print(i)

b = 'name' in spam.keys()
print(b)

print(spam.get('eggs',0))
spam.setdefault('eggs',10)
print(spam)

pprint.pprint(spam)
print(pprint.pformat(spam))

# 显示字典中所有数据的函数
def displayInventory(param):
	print("Inventory:")
	count = 0
	for key in param.keys():
		count += param[key]
		print(str(param[key])+" "+key)
	# 也可以如下：
	for k,v in param.items():
		print(str(v)+' '+k)
	print("Total number of items: "+str(count))

# 更新字典
def addToInventory(param,addedItems):
	for i in addedItems:
		param.setdefault(i,0)
		param[i] = param[i]+1

testDict = {'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}
displayInventory(testDict)

dragonLoot = ['gold coin','dagger','gold coin','gold coin','ruby']
addToInventory(testDict,dragonLoot)
displayInventory(testDict)