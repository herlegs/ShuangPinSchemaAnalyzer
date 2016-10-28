import string
import json
class InputSchema:
	__singleVowels = {"a", "e", "i", "o", "u"}
	__mapping = {"consonants":{}, "vowels":{}}

	def __loadSchema(self, path=None):
		#to be overriden
		file = reafd
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

test = InputSchema()
