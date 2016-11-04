import json
from schema import InputSchema
class XiaoHeSchema(InputSchema):
	def _load_schema(self, setting):
		setting_file = open(setting, "r")
		mapping = json.loads(setting_file.read())
		for key, value in mapping["consonants"].items():
			self._mapping["consonants"][key] = value
		for key, value in mapping["vowels"].items():
			self._mapping["vowels"][key] = value
		setting_file.close()
		return

	def __init__(self, setting = "xiaohe.json"):
		super(XiaoHeSchema, self).__init__()
		self._load_schema(setting)

#test = XiaoHeSchema()
#word = sys.argv[1]
#info = test.get_word_info(word)
#print(info)
#keys = test.get_key_presses(word)
#print(keys)
