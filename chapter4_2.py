'''转置'''

grid = [['.','.','.','.','.','.'],
		['.','0','0','.','.','.'],
		['0','0','0','0','.','.'],
		['0','0','0','0','0','.'],
		['.','0','0','0','0','0'],
		['0','0','0','0','0','.'],
		['0','0','0','0','.','.'],
		['.','0','0','.','.','.'],
		['.','.','.','.','.','.']]

k = 0
while k<len(grid[0]):
	for i in range(len(grid)):
		if i==(len(grid)-1):
			print(grid[i][k])  # 打印回车
		else:
			print(grid[i][k],end='') # 不打印回车
	k=k+1