from abc import ABCMeta, abstractmethod


class IAddress(metaclass=ABCMeta):
	@abstractmethod
	def validate_address(self):
		raise NotImplementedError()
	
	@abstractmethod
	def get(self, what):
		raise NotImplementedError()
