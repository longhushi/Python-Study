# Python-Study
Python学习笔记

Python的elif执行后，接下来的不执行

sys.exit()提前结束程序

import导入模块，另一种方式 from random import * ，使用这种形式的import语句，调用random模块中的函数时不需要random.前缀。但是，使用完整的名称会让代码更可读，所以最好使用普通形式的import语句。

for range()的开始、停止和步长参数
for i in range(12,16),打印出的是12,13,14,15
因此是从12开头，到16结束，但是不包括16

for i in range(0,10,2),打印出0到8，步长为2

None表示没有值，None是NoneType数据类型的唯一值
print()的返回值就是None

print('Hello',end='')
print('World')
输出 HelloWorld

print('cats','dogs','mice',sep=',')
输出 cats,dogs,mice

如果在函数中要修改全局变量的值，需要使用global语句，在函数表明这个变量是全局变量

异常处理
try:
except:

从第三章开始每一章的实践项目都实现一下
