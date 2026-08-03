from abc import ABCMeta, abstractmethod

class IRequest(metaclass=ABCMeta):
    
	@abstractmethod
	def get_offerings_subscription(self, callback_method):
		raise NotImplementedError()
	
	@abstractmethod
	def get_profile_subscription(self):
		raise NotImplementedError()
	
	@abstractmethod
	def set_profile_subscription(self, profile):
		raise NotImplementedError()
	
	@abstractmethod
	def set_offerings_subscription(self, offerings):
		raise NotImplementedError()