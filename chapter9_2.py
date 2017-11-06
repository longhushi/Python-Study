# 将带有美国风格日期的文件改名为欧洲风格日期
import shutil,os,re

# 美国日期格式
datePattern = re.compile(r"""^(.*?)
	((0|1)?\d)-
	((0|1|2|3)?\d)-
	((19|20)\d\d)
	(.*?)$
	""",re.VERBOSE)

# 识别文件名中的日期部分
for amerFilename in os.listdir('.'):
	mo = datePattern.search(amerFilename)
	# Skip files without a date.
	if mo == None:
		continue
	# Get the different parts of the filename.
	beforePart = mo.group(1)
	monthPart = mo.group(2)
	dayPart = mo.group(4)
	yearPart = mo.group(6)
	afterPart = mo.group(8)

	# 构成新文件名，并对文件改名
	# Form the European-style filename.
	euroFilename = beforePart+dayPart+'-'+monthPart+'-'+yearPart+afterPart
	# Get the full,absolute file paths.
	absWorkingDir = os.path.abspath('.')
	amerFilename = os.path.join(absWorkingDir,amerFilename)
	euroFilename = os.path.join(absWorkingDir,euroFilename)
	# Rename the files.
	print('Renaming "%s" to "%s"...' % (amerFilename,euroFilename))
	shutil.move(amerFilename,euroFilename)