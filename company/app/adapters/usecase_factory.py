from ..usecases.i_usecase_factory import IUsecaseFactory
from .adapater_factory import AdapterFactory
from .rest_adapter import RestAdapter
from .data_adapter import DataAdapter

class UsecaseFactory(IUsecaseFactory):
	def __init__(self, data_source):
		self.data_source = data_source # sqlalchemy_adapater
		self.adapter_factory = AdapterFactory()
		self.rest_adapter = RestAdapter(self.adapter_factory) # We want one instance of RestAdapter
		print("usecase factory created!")

	def create_request(self):
		print("Request created")
		return self.rest_adapter
	
	def create_profile(self):
		print("profile created")
		return DataAdapter(self.data_source)