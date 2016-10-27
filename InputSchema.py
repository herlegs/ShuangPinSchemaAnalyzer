import string
from sets import Set
class InputSchema:
	__singleVowels = Set(["a", "e", "i", "o", "u"])
	__mapping = {"consonants":{}, "vowels":{}}

	def __init__(self):
		for c in string.ascii_lowerletters:
			if c in __singleVowels:
				__mapping[vowels]

	def init