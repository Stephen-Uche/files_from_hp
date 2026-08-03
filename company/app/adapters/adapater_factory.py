from .i_adapater_factory import IAdapterFactory
from ..entities import Telephone, Address

class AdapterFactory(IAdapterFactory):
	def create_address(self, address):
		print("Adatper factory, create_address method", address)
		return Address(address)
	

	def create_telephone(self, phone_number):
		return Telephone(phone_number)
