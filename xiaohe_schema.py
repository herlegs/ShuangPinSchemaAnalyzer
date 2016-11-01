import json
from schema import InputSchema
class XiaoHeSchema(InputSchema):
	def _load_schema(self, path):
		setting_file = open(path, "r")
		mapping = json.loads(setting_file.read())
		for key, value in mapping["consonants"].items():
			self._mapping["consonants"][key] = value
		for key, value in mapping["vowels"].items():
			self._mapping["vowels"][key] = value
		setting_file.close()
		return

	def __init__(self, path = "xiaohe.json"):
		super(XiaoHeSchema, self).__init__()
		self._load_schema(path)