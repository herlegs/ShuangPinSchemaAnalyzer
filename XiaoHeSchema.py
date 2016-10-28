from InputSchema import *
class XiaoHeSchema(InputSchema):
	def __loadSchema(self, path="xiaohe.json"):
		#to be overriden
		return

	def __init__(self):
		InputSchema.__init__()
		self.__loadSchema()

test = XiaoHeSchema()

