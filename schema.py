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
		keys = []
		info = self.get_word_info(pinyin)
		if info["is_vowel"]:
			for char in pinyin:
				keys.append(char)
		else:
			keys.append(self._mapping["consonants"][info["consonant"]])
			vowel_index = len(info["consonant"])
			end_vowel = pinyin[vowel_index:]
			if end_vowel in self._mapping["vowels"]:
				keys.append(self._mapping["vowels"][end_vowel])
		return keys
				
	def get_word_info(self, pinyin):
		info = {"is_vowel": True, "consonant": ""}
		if pinyin and len(pinyin) > 1:
			matched_consonants = []
			for consonant in self._mapping["consonants"]:
				if pinyin.startswith(consonant):
					matched_consonants.append(consonant)
			if matched_consonants:
				info["is_vowel"] = False
				info["consonant"] = max(matched_consonants, key=len)
		return info
					
		
	def print_map(self, map):
		print(json.dumps(map, indent=4))

	def str(self):
		self.print_map(self._mapping)

# test = InputSchema()
