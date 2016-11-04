import sys
import pinyin
"pass in a string of chinese character, output a list of pinyin(single character)"
def to_pinyin(cn):
	list = []
	for char in cn.decode('utf-8'):
		list.append(pinyin.get(char, format="strip"))
	return list

def load_file(filename):
	chinese_file = open(filename, "r")
	pinyin_list = to_pinyin(chinese_file.read())
	return pinyin_list

#test = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
#print(load_file(test))
