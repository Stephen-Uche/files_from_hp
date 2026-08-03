from abc import ABCMeta, abstractmethod

from .i_request import IRequest

class IUsecaseFactory(metaclass=ABCMeta):
    
	@abstractmethod
	def create_request(self)-> IRequest:
		raise NotImplementedError()
	
	@abstractmethod
	def create_profile(self):
		raise NotImplementedError()
