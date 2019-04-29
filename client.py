from util import post


class Account(object):
	def __init__(self,name, password, port):
		self.name = name
		self.password = password
		self.port = port
	def unlock(self):
		post("unlock", [self.password], self.port)



