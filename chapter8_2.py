import re

f = open('madwords.txt')
#print(f.read())
content = f.read()
f.close()

replacewords = ['ADJECTIVE','NOUN','ADVERB','VERB']

newcontent = ''

for word in content.split(' '):
	regex = re.compile(r'\w+')
	w = regex.search(word).group()
	print(w)

	if w in replacewords:
		print('Enter an '+w.lower()+':')
		new_word = input()
		content = content.replace(w,new_word,1) # replace最后一个参数代表最多替换不超过多少次，这里选择替换一次

print(content)

fw = open('newwords.txt','w')
fw.write("转换后："+content)
fw.close()