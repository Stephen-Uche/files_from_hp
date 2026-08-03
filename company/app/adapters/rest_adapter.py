from flask import abort

from ..usecases.i_request import IRequest
from .i_rest import IRest

class RestAdapter(IRequest, IRest):
	def __init__(self, adapter_factory) -> None:
		self.adapter_factory = adapter_factory

	def rest(self, args: dict, **kwargs):
		if args["request"] == "get_offerings":
			return self.get_offerings_callback()
		if args["request"] == "get_profile":
			return self.get_profile_callback()
		if args["request"] == "get_address":
			return self.get_address_callback()
		if args["request"] == "get_core_values":
			return self.get_core_values_callback()
		if args["request"] == "set_offerings":
			offerings_to_update = self.set_offferings(kwargs)
			if offerings_to_update:
				return {
					"message": "offerings updated"
				}, 200
			abort(400)
		if args["request"] == "set_profile":
			profile_to_update = self.set_profile(kwargs)
			if profile_to_update:
				return {
					"message": "profile updated"
				}, 200
			abort(400)
		if args["request"] == "set_address":
			address_to_update = self.set_address(kwargs)
			if address_to_update:
				return {
					"message": "address updated"
				}, 200
			abort(400)
		if args["request"] == "set_core_values":
			core_values_to_update = self.set_core_values(kwargs)
			if core_values_to_update:
				return {
					"message": "core values updated"
				}, 200
			abort(400)


	def set_offferings(self, kwargs):
		offerings_to_update = kwargs.get('data').get('offerings')
		if offerings_to_update:
			return self.set_offerings_callback(offerings_to_update)


	def set_profile(self, kwargs):
		if kwargs.get("data").get("phone"):
			kwargs["data"]["phone"] = self.adapter_factory.create_telephone(kwargs["data"]["phone"])
		return self.set_profile_callback(kwargs["data"])

	
	def set_address(self, kwargs):
		if kwargs.get("data").get("address"):
			kwargs["data"]["address"] = self.adapter_factory.create_address(kwargs["data"]["address"])
		return self.set_address_callback(kwargs["data"])


	def set_core_values(self, kwargs):
		core_values_to_update = kwargs.get('data').get('core_values')
		if core_values_to_update:
			return self.set_core_values_callback(core_values_to_update)


	def get_offerings_subscription(self, callback_method):
		self.get_offerings_callback = callback_method


	def get_profile_subscription(self, callback_method):
		self.get_profile_callback = callback_method


	def get_address_subscription(self, callback_method):
		self.get_address_callback = callback_method


	def get_core_values_subscription(self, callback_method):
		self.get_core_values_callback = callback_method
	

	def set_profile_subscription(self, callback_method):
		self.set_profile_callback = callback_method

	
	def set_offerings_subscription(self, callback_method):
		self.set_offerings_callback = callback_method

	
	def set_address_subscription(self, callback_method):
		self.set_address_callback = callback_method


	def set_core_values_subscription(self, callback_method):
		self.set_core_values_callback = callback_method
