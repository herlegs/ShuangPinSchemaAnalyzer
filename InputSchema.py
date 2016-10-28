import string
import json
from abc import ABCMeta, abstractmethod
class InputSchema(metaclass=ABCMeta):
	# __metaclass__ = ABCMeta
	__singleVowels = {"a", "e", "i", "o", "u"}
	__mapping = {"consonants":{}, "vowels":{}}

	@abstractmethod
	def __loadSchema(self, path=None):
		#to be overriden
		return

	def __loadSingleChars(self):
		for c in string.ascii_lowercase:
			if c in self.__singleVowels:
				self.__mapping["vowels"][c] = c
			else:
				self.__mapping["consonants"][c] = c

	def __init__(self):
		self.__loadSingleChars(path);
		

	def str(self):
		print(json.dumps(self.__mapping, indent=4))

# test = InputSchema()
