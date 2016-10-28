from InputSchema import InputSchema
class XiaoHeSchema(InputSchema):
	def _load_schema(self, path):
		print(path)
		return

	def __init__(self, path = "xiaohe.json"):
		super(XiaoHeSchema, self).__init__()
		self._load_schema(path)

test = XiaoHeSchema()