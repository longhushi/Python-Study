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

=====================================Chapter 4

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

=====================================Chapter 5

字典是不排序的，所以不能执行切片操作

keys(),values(),items() 分别返回字典的键值，值，以及键值对。但返回的不是列表，不能排序，没有append方法

'keyname' in spam.keys() # 判断是否存在相应的键值

get()方法，有两个参数，一个是键名，一个是默认值

setdefault()，设置字典默认值，如果该键值不存在，则创建

spam.setdefault('color','black')

pprint模块，打印美化模块，pprint.pformat()

注意：'color' in spam本质上是一个简写版本。相当于'color' in spam.keys()

遍历字典，有一种简便写法：
for k,v in param.items():
  print(str(v)+' '+k)
  // To do

=====================================Chapter 6

转义字符 \'  单引号

\"  双引号

\t  制表符

\n  换行符

\\  反斜杠

原始字符串：不转义的字符串 print(r'That is Carol\'s cat.')

'''abc''' 多行字符串

"""多行注释"""

字符串也可以切片操作，也可以使用in 和 not in 操作符

upper() 字符串转成大写

lower() 字符串转成小写

isupper() 判断字符串是否都是大写

islower() 判断字符串是否都是小写

isalpha() 判断字符串是否只包含字母并且非空

isalnum() 判断字符串是否只包含数字和字母，并且非空

isdecimal() 判断字符串是否只包括数字，并且非空

isspace() 判断字符串是否只包含空格、制表符和换行，并且非空

istitle() 判断字符串是否仅包含以大写字母开头、后面都是小写字母的单词。'This Is Title Case'

startswith()和endswith() 字符串的开头和结尾

join() 连接字符串

split() 分割字符串

', '.join(['cats','rats','bats']) 返回 'cats, rats, bats'

rjust() 向左对齐

ljust() 向右对齐

center() 居中对齐

strip() 删除空白字符

rstrip() 删除右边的空白字符

lstrip() 删除左边的空白字符

pyperclip 模块拷贝粘贴字符串

import pyperclip

pyperclip.copy('Hello world!')

pyperclip.paste()

=====================================Chapter 7

正则表达式导入模块：import re

模板

import re
   regex = re.compile(r'\d\d\d-\d\d\d\d')
   mo = regex.search(str)
   print(mo.group())

mo是Match对象，加上r''代表是传递原始字符串，字符不用转义
1.用import re导入正则表达式模块。
2.用re.compile()函数创建一个Regex对象（记得使用原始字符串）
3.向Regex对象的search()方法传入想查找的字符串。它返回一个Match对象
4.调用Match对象的group()方法，返回实际匹配文本的字符串

利用括号进行分组，如(\d\d\d)-(\d\d\d\d)，group()或者group(0)返回匹配的整个文本，group(1)返回分组1，group(2)返回分组2

用管道匹配多个分组，|分隔符，例如正则表达式r'Batman|Tina Fey'匹配'Batman'或'Tina Fey'

()? 匹配零次或一次
()* 匹配零次或多次
()+ 匹配一次或多次
{}花括号匹配任意多次
(Ha){3,5}匹配3到5次
(Ha){3,}匹配3次或更多次
(Ha){,5}匹配0到5次

贪心匹配和非贪心匹配
默认贪心匹配，加上？后就是非贪心匹配
如r'(Ha){3,5}'匹配'HaHaHaHaHa',贪心匹配会匹配到'HaHaHaHaHa'，非贪心匹配会匹配到'HaHaHa'

从第三章开始每一章的实践项目都实现一下

