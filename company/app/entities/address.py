from .i_address import IAddress

class Address(IAddress):
	def __init__(self, address: dict):
		self.address = address

	def validate_address(self):
		return True
	
	def get(self, what):
		return self.address['address'][what]
	
