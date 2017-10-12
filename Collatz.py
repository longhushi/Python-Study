#《Python编程快速上手》第三章实践项目
#编写一个名为collatz()的函数，它有一个名为number的参数。如果参数是偶数那么collatz就打印出number/2，并返回该值。如果number是奇数，collatz就打印并
#返回3*number+1.
#然后编写一个程序，让用户输入一个整数，并不断对这个数调用collatz(),到函数返回值1（对于任何整数都有效）

def collatz(number):
	while number!=1:
		if number%2==0:
			print(number/2)
			number = number/2
		elif number%2==1:
			print(3*number+1)
			number = 3*number+1


# 永久循环，如果输入不是数字就提示，继续输入，直到输入正确，计算结束后跳出循环
while True:
	try:
		n = input('输入参数：')
		n = int(n)
		collatz(n)
		break;
	except ValueError:
		print('请输入一个数字！')

