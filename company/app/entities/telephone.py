from .i_telephone import ITelephone

class Telephone(ITelephone):
	def __init__(self, phone_number) -> None:
		self.phone_number = phone_number


	def validate_telephone(self):
		pass
