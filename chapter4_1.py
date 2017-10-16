spam = ['apple','bananas','tofu','cats']


def convert(paramlist):
	temp = ""

	for i in range(len(spam)):
		print(spam[i])
		if i==len(spam)-1:
			temp += "and " + spam[i]
		else:
			temp += spam[i]+", "
	return temp

result = convert(spam)
print(result)