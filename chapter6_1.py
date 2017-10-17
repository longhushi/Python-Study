tableData = [['apples','oranges','cherries','banana'],
			 ['Alice','Bob','Carol','David'],
			 ['dogs','cats','moose','goose']]

max=[]
def printTable(table):
	# 获取每行数据的最大长度
	for i in range(len(table)):
		m = 0
		for j in range(len(table[i])):
			temp = len(table[i][j])
			if temp>m:
				m = temp
		max.append(m)
	print(max)

	for k in range(len(table[0])):
		for i in range(len(table)):
			temp = table[i][k].rjust(max[i])
			print(temp,end=' ')
		print()

printTable(tableData)
