from abc import ABCMeta, abstractmethod


class IAdapterFactory(metaclass=ABCMeta):
	@abstractmethod
	def create_address(self):
		raise NotImplementedError()
	

	@abstractmethod
	def create_telephone(self):
		raise NotImplementedError()