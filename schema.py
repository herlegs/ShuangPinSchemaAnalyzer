import string
import json
from abc import ABCMeta, abstractmethod
class InputSchema(metaclass=ABCMeta):
	# __metaclass__ = ABCMeta
	__singleVowels = {"a", "e", "i", "o", "u"}
	_mapping = {"consonants":{}, "vowels":{}}

	@abstractmethod
	def _load_schema(self, path):
		#to be overriden
		return

	def __load_single_chars(self):
		for c in string.ascii_lowercase:
			if c in self.__singleVowels:
				self._mapping["vowels"][c] = c
			else:
				self._mapping["consonants"][c] = c

	def __init__(self):
		self.__load_single_chars();
		
	def get_key_presses(self, pinyin):
		
		
	def print_map(self, map):
		print(json.dumps(map, indent=4))

	def str(self):
		self.print_map(self._mapping)

# test = InputSchema()
