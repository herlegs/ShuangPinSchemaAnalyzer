from __future__ import division
import sys
import string
from xiaohe_schema import XiaoHeSchema
from getpinyin import load_file
import webcrawler

def get_key_presses(source_file, schema):
	keys = []
	pinyin_list = load_file(source_file)
	for py in pinyin_list:
		for keypress in schema.get_key_presses(py):
			keys.append(keypress)
	return keys

def show_statistics(keys):
	key_map = {}
	total_count = 0
	for key in keys:
		total_count += 1
		if key not in key_map:
			key_map[key] = 1
		else:
			key_map[key] += 1

	for k in string.ascii_lowercase:
		count = dict.get(key_map, k, 0)
		print("{0} has been pressed (out of total) {1}/{2} ({3:.2f}%)".format(k, count, total_count, count/total_count*100))

schema = XiaoHeSchema()
input_filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
#webcrawler.crawl(input_filename)
keys = get_key_presses(input_filename, schema)
show_statistics(keys)

