from abc import ABCMeta, abstractmethod


class ITelephone(metaclass=ABCMeta):
	@abstractmethod
	def validate_telephone(self):
		raise NotImplementedError()
