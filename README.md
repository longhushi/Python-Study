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

Regex对象的search()方法只返回被查找字符串中的“第一次”匹配的文本，而findall()方法将返回一组字符串，包含被查找字符串中的所有匹配。

\d 0-9的任何数字

\D 除0-9的数字以外的任何字符

\w 任何字母、数字或下划线字符

\W 除字母、数字和下划线以外的任何字符

\s 空格、制表符或换行符（可以认为是匹配空白字符）

\S 除空格、制表符和换行符以外的任何字符

建立自己的分类

[0-5]匹配数字0到5

[aeiouAEIOU]匹配元音字母

可以在正则表达式的开始处使用插入符号^，表明匹配必须发生在被查找文本开始处。类似地，可以在正则表达式的末尾加上$，表示该字符串必须以这个正则
表达式的模式结束。

通配符

. 匹配除了换行符以外的任何字符

.* 匹配所有字符，.* 总是贪心模式，要想用非贪心模式匹配，就要使用.*?

re.compile('.*',re.DOTALL) 匹配所有字符，包括换行符

sub()方法替换字符串

re.IGNORECASE（re.I） 表示忽略大小写

re.DOTALL 表示可以匹配换行符

re.VERBOSE 表示美化，可以多行写正则表达式

=====================================Chapter 8


os.path.join('usr','bin','spam') 组合路径，会根据不同的系统生成分隔符

os.getcwd()获取当前工作目录

os.chdir()改变当前工作目录

os.makedirs('C:\\delicious\\walnut\\waffles') 创建目录，路径中的所有目录都会创建一遍，如果目录已经存在了则会报错

os.path.abspath(path)获取绝对路径

os.path.isabs(path)判断是否是绝对路径

os.path.relpath(path,start)获取从start路径到path的相对路径的字符串

os.path.dirname(path) 返回path最后一个斜杠之前的所有内容

os.path.basename(path) 返回最后一个斜杠之后的内容，一般就是程序名

os.path.getsize(path) 返回path中文件的字节数

os.listdir(path) 返回path文件夹中的文件名字符串列表

os.path.exists(path) 判断路径是否存在

os.path.isdir(path) 判断路径是否是一个文件夹

f = open(filepath) 打开文件

f = open(filepath,'r',encoding='UTF-8')指定打开方式和编码格式。
r 只读 w 写入 a 追加写入

shelve模块保存变量，有点像android的sharedPreference

shelfFile = shelve.open('mydata')

cats = ['Pooka']

shelfFile['cats']=cats

shelfFile.close()

=====================================Chapter 9

shutil模块提供了一些函数，用于复制文件和整个文件夹

调用shutil.copy(source,destination)将路径source处的文件复制到路径destination处的文件夹(source和destination都是字符串)。如果destination是一个文件名，它将作为被复制文件的新名字。该函数返回一个字符串，表示被复制文件的路径。

shutil.copy()复制一个文件，shutil.copytree()复制整个文件夹，以及它包含的文件夹和文件

shutil.move()移动文件，如果目标文件夹处已经有同名的文件了，则会被覆盖

shutil.move()也可以用来修改文件名

os.unlink(path)将删除path处的文件

os.rmdir(path)将删除path处的文件夹。该文件夹必须为空，其中没有任何文件和文件夹

shutil.rmtree(path)将删除path处的文件夹，它包含的所有文件和文件夹都会被删除

以上三个函数是真删除，要慎重

可以安装send2trash模块安全的删除

使用os.walk()方法来遍历文件树

os.walk()在循环的每次迭代中返回3个值

1.当前文件夹名称字符串

2.当前文件夹中子文件夹的字符串列表

3.当前文件夹中文件的字符串的列表

for folderName,subfolders,filenames in os.walk('c:\\delicious')

需要遍历文件夹中所有文件的时候直接用这个方法就可以了，不用考虑subfolders，会自动遍历进去的

zpifile模块压缩文件

exampleZip = zipfile.ZipFile('example.zip') #读取压缩文件

exampleZip.namelist() #压缩文件中文件列表

spamInfo = exampleZip.getinfo('spma.txt') #读取压缩文件中的某一个文件

spamInfo.file_size 文件大小

spamInfo.compress_size 压缩后文件大小

exampleZip.close() 关闭压缩文件

从zip文件中解压缩

exampleZip.extractall() # 提取所有文件

exampleZip.extract('spam.txt') # 提取单个文件

exampleZip.extract('spam.txt','C:\\some\\new\\folders') # 提取单个文件到指定文件夹中

创建ZIP文件

newZip = zipfile.ZipFile('new.zip','w')

向ZIP文件中添加文件

newZip.write('spam.txt',compress_type=zipfile.ZIP_DEFLATED)

newZip.close()

从第三章开始每一章的实践项目都实现一下

字典排序

1.sorted函数按key值对字典排序

先来基本介绍一下sorted函数，sorted(iterable,key,reverse)，sorted一共有iterable,key,reverse这三个参数。

其中iterable表示可以迭代的对象，例如可以是dict.items()、dict.keys()等，key是一个函数，用来选取参与比较的元素，reverse则是用来指定排序是倒序还是顺序，reverse=true则是倒序，reverse=false时则是顺序，默认时reverse=false。

如：d={'lilee':25,'wangyan':21,'liqun':32,'lidamling':19}

sorted(d.keys())

结果是：['lidamling','lilee','liqun','wangyan']

直接使用sorted(d.keys())就能按key值对字典排序，这里是按照顺序对key值排序的，如果想按照倒序排序的话，则只要将reverse置为true即可。

2.sorted函数按value值对字典排序

要对字典的value排序则需要用到key参数，在这里主要提供一种使用lambda表达式的方法，如下：

d={'lilee':25,'wangyan':21,'liqun':32,'lidamling':19}

sorted(d.items(),key=lambda item:item[1])

结果是：[('lidamling',19),('wangyan',21),('lilee',25),('liqun',32)]

这里的d.items()实际上是将d转换为可迭代对象，迭代对象的元素为（‘lilee’,25）、（‘wangyan’,21）、（‘liqun’,32）、（‘lidaming’,19），items()方法将字典的元素转化为了元组，而这里key参数对应的lambda表达式的意思则是选取元组中的第二个元素作为比较参数（如果写作key=lambda item:item[0]的话则是选取第一个元素作为比较对象，也就是key值作为比较对象。lambda x:y中x表示输出参数，y表示lambda函数的返回值），所以采用这种方法可以对字典的value进行排序。注意排序后的返回值是一个list，而原字典中的名值对被转换为了list中的元组。

pandas的dataframe存储到excel的方法：

df.to_csv ("testfoo.csv" , encoding = "utf-8")

