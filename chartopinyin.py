import sys
def topinyin(cn):
	for char in cn.decode('utf-8'):
		print(char + ",")

topinyin(sys.argv[1])
