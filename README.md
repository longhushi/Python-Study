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

列表负数索引代表从后往前数，list[-1] 代表列表的最后一个元素
list[1:4]表示列表第二个元素到第四个元素（返回 a[1],a[2],a[3]）
list[0:-1]列表第一个到最后一个元素
list[:2]从头开始到第二个元素（返回a[0],a[1]）
list[1:]从第二个元素开始的所有元素（返回a[1]开始的所有元素）
len(list) 返回列表长度
del 删除列表中的元素
del 也可以删除变量，就像是取消赋值，但是没什么意义，用不到
in和not in 判断一个元素在不在列表中
cat=['fat','black','loud']
size,color,disposition=cat # 多重赋值，用列表一下子对几个元素赋值
index() 返回列表元素的位置
list.index('aaa') # 如果列表中不存在aaa，会报错，要用try except处理
list.append('aaa') # 在列表尾部加入元素
list.insert(1,'aaa') # 把元素插入到列表的位置1
list.remove('aaa') # 从列表中删除指定元素
list = ['aaa','bbb','ccc','aaa']
list.remove('aaa') # 删除的是第一个aaa，剩下的list是['bbb','ccc','aaa']
list.sort() # 排序
list.sort(reverse=True) # 反向排序
如果列表中有数字和字符串一起，不能调用排序，调用会报错
字符串排序是根据ASCII字符顺序的，也就是说'Z'在'a'前面，如果要严格按照字符顺序排序，需要都按小写字符排序
list.sort(key=str.lower)
元组其实就是列表的一种，只不过元组的内容不能改变，效率高一点
元组用圆括号表示，只有一个元素的元组要加一个逗号表示，('hello',)，否则会被系统认为是字符串
type(('hello',)) # <class 'tuple'>
type(('hello')) # <class 'str'>
list('hello') # 返回['h','e','l','l','o']

列表和字典，元组在函数调用时都是传递引用的
如果一个列表赋值到另一个列表，但是还希望各自改变值，要用copy模块，如果列表中还有列表，要用deepcopy()
spam = ['A','B','C','D']
cheese = copy.copy(spam)
cheese[1] = 42
最后spam的值：['A','B','C','D'],cheese的值：['A',42,'C','D']

从第三章开始每一章的实践项目都实现一下

