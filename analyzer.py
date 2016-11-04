import sys
from xiaohe_schema import XiaoHeSchema
from getpinyin import load_file

def get_key_presses(source_file, schema):
	keys = []
	pinyin_list = load_file(source_file)
	for py in pinyin_list:
		for keypress in schema.get_key_presses(py):
			keys.append(keypress)
	return keys

schema = XiaoHeSchema()
input_filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
keys = get_key_presses(input_filename, schema)
print(keys)

